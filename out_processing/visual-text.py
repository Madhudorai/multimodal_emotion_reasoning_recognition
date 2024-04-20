import pandas as pd

# Read CSV file
df = pd.read_csv("/Users/swarsys/Documents/FINALYEARPROJECT/processed/dia1_utt0.csv")

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
with open('/Users/swarsys/Documents/FINALYEARPROJECT/processed/max_columns.txt', 'w') as txt_file:
    for column_name in max_columns:
        txt_file.write(column_name + '\n')


