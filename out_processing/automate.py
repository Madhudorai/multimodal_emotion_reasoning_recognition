import os
import subprocess
import pandas as pd
from visualtext import process_csv, run_openface 
from llama2 import generate_response

def main(video_folder, data_csv_file, results_csv_file):
    data = []  # List to store data for CSV file
    
    # Create results directory if it doesn't exist
    output_dir = os.path.dirname(results_csv_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterate over the files in the video folder
    for video_file in os.listdir(video_folder):
        if video_file.endswith(".mp4"):
            # Construct the full path to the video file
            input_video_path = os.path.join(video_folder, video_file)
            
            # Run OpenFace and extract features
            run_openface(input_video_path)
            
            # Extract video name without extension
            filename = os.path.basename(input_video_path)
            video_name = os.path.splitext(filename)[0]

            # Process the CSV file to get max columns
            csv_path = os.path.join("processed", video_name + ".csv")
            process_csv(csv_path)

            # Extract video name and the corresponding row in the DataFrame
            dia_number, utt_number = map(int, video_name.split("_")[-1][3:])
            df = pd.read_csv(data_csv_file)
            row = df[(df['Dialogue_ID'] == dia_number) & (df['Utterance_ID'] == utt_number)]
            utterance = row["Utterance"].values[0]  # Get the value from the DataFrame
            
            # Construct the prompt
            prompt_template = "Facial action units activated in the speaker over time: {max_columns}\n" \
                            "utterance of speaker: {utterance}\n" \
                            "What is the speaker's emotion and reasoning for the same?\n" \
                            "Finally, choose 1 emotion out of 7 - surprise, fear, anger, joy, neutral, sadness, disgust,\n" \
                            "and choose 1 out of 3 sentiments - neutral, positive, negative, that match the speaker's face and utterance."
            prompt = prompt_template.format(max_columns="processed/max_columns.txt", utterance=utterance)

            # Generate response using llama
            output_text = generate_response(prompt)

            # Append data to list
            data.append([input_video_path, utterance, prompt, output_text])
    
    # Convert data list to DataFrame
    df_output = pd.DataFrame(data, columns=['Input_Video_Path', 'Utterance', 'Prompt', 'Generated_Response'])

    # Save DataFrame to CSV file
    df_output.to_csv(results_csv_file, index=False)
    
    # Delete max_columns.txt file
    max_columns_path = "processed/max_columns.txt"
    if os.path.exists(max_columns_path):
        os.remove(max_columns_path)

# Example usage:
video_folder = "/Users/swarsys/Documents/YP/testvideos"
csv_file = "data/train/train_sent_emo.csv"
results_csv_file = "results/output_data.csv"
main(video_folder, csv_file, results_csv_file)


