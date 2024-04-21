import pandas as pd
import subprocess

def run_openface(input_video_path):
    command = f"Openface/build/bin/FeatureExtraction -f \"{input_video_path}\""
    subprocess.run(command, shell=True)

def process_csv(csv_path):
    # Read CSV file
    df = pd.read_csv(csv_path)

    # Define the mapping of AU codes to their corresponding facial action descriptions
    au_mapping = {
        'AU01_r': 'Inner Brow Raised',
        'AU02_r': 'Outer Brow Raised',
        'AU04_r': 'Brow Lowerer',
        'AU05_r': 'Upper Lid Raiser',
        'AU06_r': 'Cheek Raiser',
        'AU07_r': 'Lid Tightener',
        'AU09_r': 'Nose Wrinkler',
        'AU10_r': 'Upper Lip Raiser',
        'AU12_r': 'Lip Corner Puller',
        'AU14_r': 'Dimpler',
        'AU15_r': 'Lip Corner Depressor',
        'AU17_r': 'Chin Raiser',
        'AU20_r': 'Lip Stretcher',
        'AU23_r': 'Lip Tightener',
        'AU25_r': 'Lips Part',
        'AU26_r': 'Jaw Drop',
        'AU28_r': 'Lip Suck',
        'AU45_r': 'Blink'
    }

    # List of columns to keep
    columns_to_keep = ['frame', 'face_id', 'timestamp'] + list(au_mapping.keys())

    # Filter DataFrame to keep only required columns and rename them
    modified_df = df.filter(columns_to_keep).rename(columns=au_mapping)

    # Find the column with the maximum value in each row
    max_columns = modified_df.drop(['frame', 'face_id', 'timestamp'], axis=1).idxmax(axis=1)

    # Write the max column names to a text file
    max_columns_path = "/".join(csv_path.split("/")[:-1]) + "/max_columns.txt"
    with open(max_columns_path, 'w') as txt_file:
        txt_file.write(", ".join(max_columns))

    # Write the modified DataFrame to a new CSV file
    output_csv_path = "/".join(csv_path.split("/")[:-1]) + "/processed_" + csv_path.split("/")[-1]
    modified_df.to_csv(output_csv_path, index=False)

    return output_csv_path






