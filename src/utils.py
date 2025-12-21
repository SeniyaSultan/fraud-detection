import pandas as pd

def safe_load_csv(path):
    """Load a CSV safely, returns None if file not found."""
    try:
        df = pd.read_csv(path)
        print(f"Loaded data with shape {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return None

def check_columns(df, required_columns):
    """Check if required columns exist in DataFrame."""
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in DataFrame: {missing}")
    return True

def print_separator(title=None):
    """Print a clean separator line for console output."""
    if title:
        print(f"\n=== {title} ===\n")
    else:
        print("\n" + "="*40 + "\n")
