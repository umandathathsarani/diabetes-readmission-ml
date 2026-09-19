import pandas as pd
from pathlib import Path

def load_raw_data():
    data_path = Path('../../data/raw/diabetic_data.csv')
    df = pd.read_csv(data_path)
    return df
