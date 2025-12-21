import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return None

def preprocess(df):
    df = df.dropna()  # basic cleaning
    df['country'] = df['country'].astype('category').cat.codes
    return df
