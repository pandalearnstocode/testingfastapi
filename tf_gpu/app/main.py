from fastapi import FastAPI, File, UploadFile
import joblib
import os
import pathlib
import pandas as pd
import codecs
import csv
from gpu_test import gpu_check
from utils import RawRequest
from utils import compress_files
from utils import train_tf_model
from utils import model_response
import json
import pickle

PYMMM_VERSION = "0.0.1"

app = FastAPI()


@app.post("/savefile")
def save(file: UploadFile = File(...)):
    gpu_check()
    data_dir = pathlib.Path(os.path.join(".", "data"))
    if file.filename.endswith(".csv"):
        csv_reader = csv.reader(codecs.iterdecode(file.file, "utf-8"))
        df = pd.DataFrame(csv_reader)
        model_id = joblib.hash(df)
        file_name = model_id + ".csv"
        file_full_path = pathlib.Path(os.path.join(data_dir, file_name))
        df.to_csv(f"{file_full_path}", index=None)
        return model_id


@app.get("/model/{model_id}")
def read_item(model_id):
    gpu_check()
    data_dir = pathlib.Path(os.path.join(".", "data"))
    file_name = model_id + ".csv"
    file_full_path = pathlib.Path(os.path.join(data_dir, file_name))
    df = pd.read_csv(file_full_path)
    return {"df_heads": df.columns.tolist()}


@app.post("/train_model")
def train_model_1(raw_req: RawRequest):
    raw_request_dict = raw_req.dict()
    country = raw_request_dict["country"]
    use_files = raw_request_dict["use_files"]
    file_types = raw_request_dict["file_types"]
    data_info_hashed, filtered_data_info_hashed = compress_files(
        country, file_types, use_files
    )
    hashed_req = {
        "raw_req": raw_request_dict,
        "filtered_data_info": filtered_data_info_hashed,
        "code_version": PYMMM_VERSION,
    }
    model_hash = joblib.hash(hashed_req)

    request_file_name = model_hash + "_request.json"
    response_file_name = model_hash + "_response.json"
    model_file_name = model_hash + "_model.pickle"
    req_path = pathlib.Path(os.path.join(".","IO", country,"request",request_file_name))
    model_path  = pathlib.Path(os.path.join(".","model", country,model_file_name))
    res_path = pathlib.Path(os.path.join(".","IO", country,"response",response_file_name))
    if not res_path.is_file():
        print("*********************")
        print("Training Model")
        print("*********************")
        if not req_path.is_file():
            with open(req_path, 'w') as fp:
                json.dump(hashed_req, fp)
        if not model_path.is_file():
            model_obj = train_tf_model(hashed_req)
            with open(model_path, 'wb') as fp:
                pickle.dump(model_obj, fp, protocol=pickle.HIGHEST_PROTOCOL)
        if not res_path.is_file():
            model_res_obj = model_response(model_obj)
            with open(res_path, 'w') as fp:
                json.dump(model_res_obj, fp)
    else:
        print("*********************")
        print("Using cached results.")
        print("*********************")
        with open(res_path, 'r') as fp:
            model_res_obj = json.load(fp)
    return {
        "request_file_name": request_file_name,
        "response_file_name": response_file_name,
        "model_file_name": model_file_name,
        "model_id":model_hash,
        "model_response":model_res_obj
    }

