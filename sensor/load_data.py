import csv
import glob
import os
import pandas as pd


def load_sensor_data():
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
    sensor_data = {}
    for sensor_file in sensor_files:
        sensor_name = os.path.splitext(os.path.basename(sensor_file))[0]
        with open(sensor_file) as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row
            data = []
            for row in reader:
                # print(row)
                data.append(row)
            sensor_data[sensor_name] = data
            # print(f"Loaded {len(data)} records from {sensor_name}")
    return sensor_data


def load_sensor_data_with_pandas() -> dict:
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
    sensor_data:dict = {}
    for sensor_file in sensor_files:
        sensor_name:str = os.path.splitext(os.path.basename(sensor_file))[0]
        data:list = pd.read_csv(sensor_file)
        sensor_data[sensor_name] = data
        print(f"Loaded {len(data)} records from {sensor_name}")
    return sensor_data
