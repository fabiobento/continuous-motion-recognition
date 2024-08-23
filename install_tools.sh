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
