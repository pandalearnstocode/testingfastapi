from fastapi import FastAPI, File, UploadFile
import joblib
import os
import pathlib
import pandas as pd
import codecs
import csv

app = FastAPI()

@app.post("/savefile")
def save(file: UploadFile = File(...)):
    data_dir = pathlib.Path(os.path.join('.','data'))
    if file.filename.endswith('.csv'):
        csv_reader = csv.reader(codecs.iterdecode(file.file,'utf-8'))
        df = pd.DataFrame(csv_reader)
        model_id = joblib.hash(df)
        file_name = model_id + ".csv"
        file_full_path = pathlib.Path(os.path.join(data_dir,file_name))
        df.to_csv(f"{file_full_path}", index = None)
        return model_id

@app.get("/model/{model_id}")
def read_item(model_id):
    data_dir = pathlib.Path(os.path.join('.','data'))
    file_name = model_id + ".csv"
    file_full_path = pathlib.Path(os.path.join(data_dir,file_name))
    df = pd.read_csv(file_full_path)
    return {"df_heads": df.columns.tolist()}