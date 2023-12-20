sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

sudo apt install docker-ce
sudo systemctl status docker

sudo usermod -aG docker ${USER}
su - ${USER}
sudo usermod -aG docker simao


docker pull rishubi/codegeex:latest #7.51 GB

#Remove all containers (on and off)
docker rm $(docker ps -aq)

#Envia a pasta com as samples dos modelos e coloca no path dentro do container "/workspace/CodeGeeX/generated_samples/"
docker run -v $(pwd)/generated_samples:/workspace/CodeGeeX/generated_samples/ -it rishubi/codegeex
