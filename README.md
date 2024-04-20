# 1. using Homebrew, a package manager for macOS and Linux, to install various software packages for setting up a development environment
brew update
brew install gcc 
brew install boost
brew install tbb
brew install openblas
brew install --build-from-source dlib
brew install wget
brew install opencv

# 2. clone repo [https://github.com/Madhudorai/YP.git]

# 3. Build
cd OpenFace
mkdir build
cd build
cmake -D WITH_OPENMP=ON CMAKE_BUILD_TYPE=RELEASE ..  
make
cd ..
bash download_models.sh 
cp lib/local/LandmarkDetector/model/patch_experts/*.dat build/bin/model/patch_experts/
