#!/bin/bash

# Instalação de pacotes básicos
sudo apt-get update
sudo apt-get install -y \
    curl \
    npm \
    git \
    nano \
    python3 \
    python3-pip \
    default-jdk \
    build-essential \
    g++
sudo rm -rf /var/lib/apt/lists/*

# Configuração de pip para usar espelhos chineses
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# Download e instalação do Go
sudo curl -o /usr/local/go.tar.gz -SL https://golang.org/dl/go1.18.4.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf /usr/local/go.tar.gz
sudo rm /usr/local/go.tar.gz
export PATH=/usr/local/go/bin:$PATH

# Download e instalação do Node.js e js-md5
sudo curl -o /usr/local/node.tar.gz -SL https://nodejs.org/download/release/v16.14.0/node-v16.14.0-linux-x64.tar.gz
sudo mkdir -p /usr/local/lib/nodejs
sudo tar -C /usr/local/lib/nodejs -xzf /usr/local/node.tar.gz
sudo mv /usr/local/lib/nodejs/node-v16.14.0-linux-x64 /usr/local/lib/nodejs/node
sudo rm /usr/local/node.tar.gz
sudo npm install -g js-md5@0.7.3
export PATH=/usr/local/lib/nodejs/node/bin:$PATH
export NODE_PATH=/usr/local/lib/node_modules

# Download e instalação do Boost
sudo curl -o /usr/local/boost.tar.gz -SL https://boostorg.jfrog.io/artifactory/main/release/1.71.0/source/boost_1_71_0.tar.gz
sudo tar -C /usr/local -xzf /usr/local/boost.tar.gz
sudo rm /usr/local/boost.tar.gz
cd /usr/local/boost_1_71_0
sudo ./bootstrap.sh --prefix=/usr/
sudo ./b2
sudo ./b2 install
cd /usr/local
sudo rm -r /usr/local/boost_1_71_0

# Download e instalação do OpenSSL
sudo curl -o /usr/local/openssl.tar.gz -SL https://www.openssl.org/source/old/3.0/openssl-3.0.0.tar.gz
sudo tar -C /usr/local -xzf /usr/local/openssl.tar.gz
sudo rm /usr/local/openssl.tar.gz
cd /usr/local/openssl-3.0.0
sudo ./Configure
sudo make
sudo make install
cd /usr/local
sudo rm -r /usr/local/openssl-3.0.0
export PATH=/usr/local/bin:$PATH

# Download e instalação do JDK
sudo curl -o /usr/local/jdk.tar.gz -SL https://download.oracle.com/java/18/latest/jdk-18_linux-x64_bin.tar.gz
sudo mkdir /usr/java
sudo tar -C /usr/java -xzf /usr/local/jdk.tar.gz
sudo rm /usr/local/jdk.tar.gz
java_path=$(sudo ls /usr/java)
sudo echo "export JAVA_HOME=/usr/java/${java_path}" >> ~/.bashrc

# Configuração final
sudo ln -sf $JAVA_HOME/bin/java /usr/bin/java
#sudo update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000
#sudo update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac 20000

# Se precisar ajustar o ambiente
source ~/.bashrc

# Permissão para criar pastas e ficheiros
chmod 700 CodeGeeX/