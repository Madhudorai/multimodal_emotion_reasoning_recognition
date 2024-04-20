import os
import csv
import opensmile

def extract_opensmile_features(mp4_file, output_csv):
    smile = opensmile.Smile(
        feature_set=opensmile.FeatureSet.eGeMAPSv02,
        feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
    )

    # Convert mp4 to wav
    wav_file = mp4_file.replace('.mp4', '.wav')
    os.system(f'ffmpeg -i {mp4_file} {wav_file}')

    # Process wav file with OpenSMILE
    feature = smile.process_file(wav_file)

    # Remove the generated wav file after processing
    os.remove(wav_file)

    # Extract feature names and values
    feature_names = feature.columns.tolist()
    feature_values = feature.values.flatten()

    # Create dictionary with feature names as keys and values as values
    features_dict = {name: value for name, value in zip(feature_names, feature_values)}

    # Write features to CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=feature_names)
        writer.writeheader()
        writer.writerow(features_dict)

# Example usage:
mp4_file_path = '/Users/swarsys/Documents/FINALYEARPROJECT/testvideos/dia1_utt0.mp4'
output_csv = '/Users/swarsys/Documents/FINALYEARPROJECT/processed/audio.csv'
extract_opensmile_features(mp4_file_path, output_csv)
