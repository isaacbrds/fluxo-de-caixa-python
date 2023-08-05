#!/bin/bash

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r bundle.txt


if [ $? eq 0 ]; then
  echo "Instalação concluida com sucesso!"
else
  echo "Houve um erro na instalação."
fi