from pathlib import Path
from datetime import datetime

import pandas as pd


def analyze_data() -> None:
    """This function read all available csv data
    Analyze for bad data, output clean data to output folder
    output bad data to a separate csv for manual intervention
    """

    # Path definitions and directory creation, skip if already exists
    current_dir = Path(__file__).parent
    project_root = current_dir.parent
    input_data_path = project_root / "data" / "input"
    input_data_path.mkdir(exist_ok=True)
    bad_data_path = project_root / "data" / "bad_data"
    bad_data_path.mkdir(exist_ok=True)
    output_data_path = project_root / "data" / "output"
    output_data_path.mkdir(exist_ok=True)
    processed_data_path = project_root / "data" / "processed_files"
    processed_data_path.mkdir(exist_ok=True)

    # Get all csv files
    input_files = [file for file in input_data_path.rglob("*.csv")]

    if not input_files:
        return "No files to process"

    # Time setting for saving files
    today_time = datetime.now()
    today_time_str = today_time.strftime("%Y-%m-%d_%H-%M-%S")

    # List to append all data
    all_data = []
    all_bad_data = []

    # Iteration for every file available to process
    for file in input_files:
        data = pd.read_csv(file.resolve(), comment="#")

        # Format normalization
        data["status"] = data["status"].str.lower()

        # Bad data searching
        bad_data = data[data["price"] < 0]

        # If bad data, remove and place in different folder for manual treatement
        if not bad_data.empty:
            data = data.drop(bad_data.index)
            all_bad_data.append(bad_data)

        all_data.append(data)

        # Move the file to processed folder
        file.replace(processed_data_path / f"orders{today_time_str}.csv")

    # Generate all data collection and write to files
    all_data_concat = pd.concat(all_data, ignore_index=True)
    all_data_concat = all_data_concat.set_index("order_id")

    all_bad_data_concat = pd.concat(all_bad_data, ignore_index=True)
    all_bad_data_concat = all_bad_data_concat.set_index("order_id")

    all_data_concat.to_csv(output_data_path / f"output_{today_time_str}.csv")
    all_bad_data_concat.to_csv(bad_data_path / f"bad_data_{today_time_str}.csv")

    return {
        "rows_processed: ": len(all_data_concat),
        "bad_rows_encountered: ": len(all_bad_data_concat),
    }
