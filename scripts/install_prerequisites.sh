#!/bin/bash

echo "Installing cargo 1.75.0..."
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

# Ensure the correct version of cargo is installed
cargo --version
required_cargo_version="1.75.0"
current_cargo_version=$(cargo --version | awk '{print $2}')

if [[ "$current_cargo_version" == "$required_cargo_version" ]]; then
  echo "Cargo $required_cargo_version is already installed."
else
  echo "Cargo version mismatch. Please ensure version $required_cargo_version is installed."
  exit 1
fi

echo "Installing cmake 3.22.1..."

# Remove any existing version of cmake if needed
sudo apt remove --purge cmake -y

# Install cmake version 3.22.1 (You may need to add specific repository or download binary if it's not available)
sudo apt update
sudo apt install -y wget
wget https://github.com/Kitware/CMake/releases/download/v3.22.1/cmake-3.22.1-linux-x86_64.tar.gz
tar -zxvf cmake-3.22.1-linux-x86_64.tar.gz
sudo mv cmake-3.22.1-linux-x86_64 /opt/cmake
sudo ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake

# Verify CMake version
cmake --version
required_cmake_version="3.22.1"
current_cmake_version=$(cmake --version | head -n 1 | awk '{print $3}')

if [[ "$current_cmake_version" == "$required_cmake_version" ]]; then
  echo "CMake $required_cmake_version is successfully installed."
else
  echo "CMake version mismatch. Please ensure version $required_cmake_version is installed."
  exit 1
fi

echo "Installing Python 3.10.12..."

# Install dependencies
sudo apt update
sudo apt install -y software-properties-common

# Add the repository and install Python 3.10
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install -y python3.10 python3.10-venv python3.10-dev

# Verify Python version
python3.10 --version
required_python_version="3.10.12"
current_python_version=$(python3.10 --version | awk '{print $2}')

if [[ "$current_python_version" == "$required_python_version" ]]; then
  echo "Python $required_python_version is successfully installed."
else
  echo "Python version mismatch. Please ensure version $required_python_version is installed."
  exit 1
fi

# Install the `weggli` tool using cargo
echo "Installing weggli using cargo..."

cargo install weggli --rev=9d97d462854a9b682874b259f70cc5a97a70f2cc --git=https://github.com/weggli-rs/weggli

echo "Installation complete."
