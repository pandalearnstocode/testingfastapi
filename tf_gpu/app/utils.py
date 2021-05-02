import glob
import pyarrow.csv as pv
import pathlib
import joblib
from pydantic import BaseModel
from typing import *
from datetime import date
import os
import pandas as pd
import time


class RawRequest(BaseModel):
    country: str
    use_files: List[str]
    file_types: str
    hierarchy_columns: List[str]
    shared_column: str
    brand_column: str
    date_column: str
    revenue_column: str
    vehicle_column: str
    sub_vehicle_column: str
    spend_column: str
    raw_power_columns: List[str]
    n_simulated_environments: int
    n_train: int
    min_contiguous: int
    dbg: bool
    visualize: int
    COVID_CUTOFF: str
    dynamics_layers: List[Dict[str, Union[str, List[str]]]]


def file_by_country(country, csv_files):
    filtered_files = [
        csv_file
        for csv_file in csv_files
        if ((csv_file.find(country) > 0) and (csv_file.find("raw") > 0))
    ]
    return filtered_files


def get_filtered_data_hashed_dict(data_info_hashed, use_data):
    dict_collector = {}
    for k, v in data_info_hashed.items():
        for k1, v1 in v.items():
            if k1 in use_data:
                dict_collector[k] = {k1: v1}
    return dict_collector


def compress_files(country, file_type, use_data):
    name_collector = []
    hash_collector = []
    compressed_files = []
    csv_files = glob.glob(f"**/*.{file_type}", recursive=True)
    csv_files = file_by_country(country=country, csv_files=csv_files)
    for csv_file in csv_files:
        csv_file = pathlib.Path(os.path.join(".", csv_file))
        df = pd.read_csv(csv_file)
        file_name = pathlib.Path(csv_file).stem
        file_hash = joblib.hash(df)
        compressed_file_name = pathlib.Path(
            (str(csv_file).replace(file_name, file_hash + "_" + file_name)).replace(
                ".csv", ".parquet.gzip"
            ).replace('raw','compressed_data')
        )
        name_collector.append(file_name)
        hash_collector.append(file_hash)
        compressed_files.append(str(compressed_file_name))
        df.to_parquet(compressed_file_name, compression="gzip", index=None)
    data_info_hashed = {
        k: {m: n} for k, m, n in zip(hash_collector, name_collector, compressed_files)
    }
    filtered_data_info_hashed = get_filtered_data_hashed_dict(
        data_info_hashed, use_data
    )
    return data_info_hashed, filtered_data_info_hashed


def train_tf_model(hashed_req):
    time.sleep(5)
    return {"model_training_status":"successful"}

def model_response(model):
    return {"dummy_response":"generated"}

