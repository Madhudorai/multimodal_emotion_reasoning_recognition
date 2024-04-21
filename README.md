## MAC INSTALLATION

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

