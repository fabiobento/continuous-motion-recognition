#!/bin/bash

# Verifica se o Python está instalado
if command -v python3 &>/dev/null; then
    echo "Python3 já está instalado."
else
    echo "Python3 não encontrado. Instale o Python3 antes de prosseguir."
    exit 1
fi

# Verifica se o pip está instalado
if command -v pip3 &>/dev/null; then
    echo "pip3 já está instalado."
else
    echo "pip3 não encontrado. Instalando pip3..."
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

# Instala o pyserial usando pip
echo "Instalando pyserial..."
pip3 install pyserial

# Verifica se a instalação foi bem-sucedida
if python3 -c "import serial" &>/dev/null; then
    echo "pyserial instalado com sucesso!"
else
    echo "Houve um problema na instalação do pyserial."
fi

# Instala o curl
echo "Instalando curl..."
sudo apt install -y curl

# Configura o Node.js 20.x
echo "Configurando Node.js..."
curl -sL https://deb.nodesource.com/setup_20.x | sudo -E bash -

# Instala o Node.js
echo "Instalando Node.js..."
sudo apt-get install -y nodejs

# Verifica a versão do Node.js instalada
echo "Verificando versão do Node.js..."
node_version=$(node -v)
echo "Node.js versão $node_version instalado com sucesso!"

# Cria o diretório para o prefixo global do npm
echo "Criando diretório ~/.npm-global..."
mkdir -p ~/.npm-global

# Configura o npm para usar o novo diretório como prefixo
echo "Configurando o npm para usar ~/.npm-global como prefixo..."
npm config set prefix '~/.npm-global'

# Adiciona ~/.npm-global ao PATH (opcional, para que comandos npm estejam disponíveis no terminal)
if ! grep -q 'export PATH=~/.npm-global/bin:$PATH' ~/.bashrc; then
    echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
    source ~/.bashrc
    echo "O PATH foi atualizado para incluir ~/.npm-global/bin."
else
    echo "O PATH já inclui ~/.npm-global/bin."
fi

# Instala o edge-impulse-cli usando npm com --force
echo "Instalando edge-impulse-cli globalmente com --force..."
sudo npm install -g edge-impulse-cli --force

# Instala o edge-impulse-linux
echo "Instalando edge-impulse-linux..."
sudo npm install -g edge-impulse-linux --force

# Instala os pacotes necessários para o PyAudio
echo "Instalando dependências do PyAudio..."
sudo apt-get install -y portaudio19-dev

# Instalar o open-cv
pip install opencv-python

# Instala a biblioteca do Edge Impulse Linux SDK for Python
pip install pyaudio edge_impulse_linux

echo "Instalação concluída!"
