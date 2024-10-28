### Repository for the thesis 2023-2024

### Documentos da tese
| Documentos                  | Links                                                                                                       |
|:---------------------------:|:-----------------------------------------------------------------------------------------------------------:|
| Plano de dissertação        | [aqui](https://github.com/simaocunha71/thesis-repository/blob/main/docs/Plano%20Disserta%C3%A7%C3%A3o.pdf)  |
| RPD                         | [aqui](https://github.com/simaocunha71/thesis-repository/blob/main/docs/RPD.pdf)                            |
| Apresentação do RPD         | [aqui](https://github.com/simaocunha71/thesis-repository/blob/main/docs/Apresenta%C3%A7%C3%A3o%20RPD.pdf)   |


### Comandos úteis para o cluster

#### Instalação do llama-cpp-python
```bash
CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip3 install llama-cpp-python
```

#### Docker images
##### HumanEval-x
```bash
docker pull alcunha71/humaneval_x:latest
```

#### Cuidados a ter no codefuseeval
##### import sacrebleu as scb
```bash
nano /home/simao/.cache/huggingface/modules/evaluate_modules/metrics/sacrebleu/0cc3ee582c27f193445865d2cdfb25edd3582d7966b11db6123c03f7f68a1a35/sacrebleu.py
```
##### pode ser preciso escrever
```bash
pip3 install sacrebleu --upgrade
```