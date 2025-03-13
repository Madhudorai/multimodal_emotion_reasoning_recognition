## MULTIMODAL EMOTION REASONING AND RECOGNITION 

# Description of Project 
Affective computing task of emotion recognition in multimodal data (video, audio, language). We test on MELD- MELD has more than 1400 dialogues and 13000 utterances from Friends TV series. Multiple speakers participated in the dialogues. Each utterance in a dialogue has been labeled by any of these seven emotions -- Anger, Disgust, Sadness, Joy, Neutral, Surprise and Fear. MELD also has sentiment (positive, negative and neutral) annotation for each utterance. https://affective-meld.github.io/ can be downloaded from here. 

Our approach is instead of using fusion mechanisms on the unimodality encoders, we textualize visual and accoustic encodings and feed it into a large language model (here, LLama-2-7B). The prompts include information about the facial action units activated in the speaker over time (extracted from the OpenFace output) and the corresponding utterance of the speaker. The response from LLM analyzes the speaker's emotion and reasoning based on their facial expressions and utterances.

![image](https://github.com/user-attachments/assets/662684c6-38b8-4761-a738-897077799fe2)

## Setup and running the project 
# 1. Environment
using Homebrew, a package manager for macOS and Linux, to install various software packages for setting up a development environment. use bin bash commands:
brew update

brew install gcc 

brew install boost

brew install tbb

brew install openblas

brew install --build-from-source dlib

brew install wget

brew install opencv

brew install ffmpeg@6
Install additional libraries (transformers, huggingface,pandas, numpy,etc)

# 2. cloning
Clone repo [https://github.com/Madhudorai/YP.git] 

# 3. Build
cd OpenFace

mkdir build

cd build

cmake -D WITH_OPENMP=ON CMAKE_BUILD_TYPE=RELEASE .. 

make

cd ..

bash download_models.sh 

cp lib/local/LandmarkDetector/model/patch_experts/*.dat build/bin/model/patch_experts/

# 4. Testing on MELD dataset
Run the automate.py script. 
Pass in 2 folders: folder with videos, csv file which contains utterance of speaker, along with episode number, speaker name as well as true labels. Video name, extracted facial features, corresponding utterance (prompt) gets stored in csv along with LLama model's emotional reasoning response. 

