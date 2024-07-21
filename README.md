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

#### Cuidados a ter no codefuse.ai
##### import sacrebleu as scb
```bash
nano /home/simao/.cache/huggingface/modules/evaluate_modules/metrics/sacrebleu/0cc3ee582c27f193445865d2cdfb25edd3582d7966b11db6123c03f7f68a1a35/sacrebleu.py
```
##### pode ser preciso escrever
```bash
pip3 install sacrebleu --upgrade
```

#### Notas do Francisco sobre o RPD - A alterar para o documento final
- Abstract e Resumo:
    - se achares relevante, inclui uma frase a falar dos modelos com quantization e dizer que queremos ver as diferenças entre os diferentes tamanhos e a eficácia/energia (como achares melhor, fica ao teu critério). [DESENVOLVER UM POUCO MELHOR PARA O DOCUMENTO FINAL]

- Introduction:
    - Context:
        - No fim "which model is the most sustainable for solving a particular problem." está fixe. Se conseguires elaborar uma pequena frase sobre o que significa ser sustentável, ficava bem. Isto é, sustentabilidade é um conceito multi-facetado: usa menos energia? requer menos manutenção? um sistema é mais fácil de compreender? é economicamente sustentável? Isto não é prioritário, se não incluíres agora fica para pensar mais para a frente :) [DESENVOLVER UM POUCO MELHOR PARA O DOCUMENTO FINAL]
    - Motivation:
        - Eu acho que a motivação está muito focada em sustentabilidade ambiental. É um dos focos mas acho que não nos devíamos prender a ele. Novamente, sustentabilidade é um conceito amplo. Mas se vires que interfere muito com o resto do documento, fica para mudarmos mais para a frente na dissertação. Fica já a nota, de qualquer das formas. [DESENVOLVER UM POUCO MELHOR PARA O DOCUMENTO FINAL]
    
- State of the Art:
    - Large Language Models:
        - "These models derive their efficacy from being ”large” indicating extensive training on vast datasets." eu debati-me um bocado com isto a escrever a minha tese. Acabei por dizer que são "large" por serem treinados com muitos dados e por terem um tamanho grande (muitos parâmetros). Para mim faz sentido mas de facto a maior parte dos recursos "só" fala da qtd dos dados. [DESENVOLVER UM POUCO MELHOR PARA O DOCUMENTO FINAL]

    - Large Language Models for Code:
        - Alguns trabalhos de repair com LLMs (não tens de ler, é só para diversificar mais as citações; são recentes e de boas confs; pode ficar para mais tarde): [DESENVOLVER UM POUCO MELHOR PARA O DOCUMENTO FINAL]
            - https://dl.acm.org/doi/abs/10.1145/3623476.3623522
            - https://ieeexplore.ieee.org/abstract/document/9401997
            - https://dl.acm.org/doi/abs/10.1145/3540250.3549101
            - https://ieeexplore.ieee.org/abstract/document/10172781
    
- The Problem and Its Challenges:
    - já que falas de armazenamento, podes incluir também um parágrafo sobre recursos para correr os modelos e.g. GPUs e VRAM/RAM [DESENVOLVER UM POUCO MELHOR PARA O DOCUMENTO FINAL]


- Experiments:
    - Já agora, estava a ler o que fizeste para minimizar o consumo de energia. Como o foco é em comparação de LLMs e não tanto em ter os valores absolutos, há coisas que não precisas de fazer. Por exemplo, o brilho do ecrã desde que seja sempre o mesmo durante as experiência, tudo bem. A internet já é melhor desligar sempre porque pode haver mais transferências a ocorrer durante um benchmark do que noutro. [DESENVOLVER UM POUCO MELHOR PARA O DOCUMENTO FINAL]
