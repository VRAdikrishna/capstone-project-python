import pandas as pd
from pathlib import Path

def load_and_validate_data(data_path='data/'):
    data_dir = Path(data_path)
    all_files = data_dir.glob('*.csv')

    combined_df = pd.DataFrame()
    errors = []

    for file in all_files:
        try:
            df = pd.read_csv(file, on_bad_lines='skip')
            df['building'] = file.stem
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
            df = df.dropna(subset=['timestamp','kwh'])
            combined_df = pd.concat([combined_df, df], ignore_index=True)
        except Exception as e:
            errors.append(str(e))

    print("Ingestion completed.")
    print("Errors:", errors)
    return combined_df
