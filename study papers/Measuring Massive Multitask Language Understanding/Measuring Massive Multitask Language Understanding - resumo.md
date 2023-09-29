#### Measuring Massive Multitask Language Understanding - Resumo

##### Abstract
- Medição de accuracy de vários NLPMs (Natural Language Processing models) através da execução de 57 tarefas que incluem os ramos da matemática básica, história dos EUA, computer sciente, direito, ...
- Dos modelos considerados, o GPT-3 é o que tem melhor accuracy
- Ainda existe muita aleatoriedade nas respostas dadas pelos modelos

##### Benchmarks referenciados
- SuperGLUE: entendimento linguístico
- HellaSwag: senso-comum
- MMLU: Massive multitask benchmark (o criado pelos autores do artigo) - https://github.com/hendrycks/test
- Physical IQA: Physical Interaction Question Answering - https://yonatanbisk.com/piqa/
- CosmosQA: Machine Reading Comprehension with Contextual Commonsense Reasoning - https://wilburone.github.io/cosmos/

##### Introdução

- NLPMs têm uma performance abaixo da obtida pelos humanos em tarefas de entendimento de linguagens
- O benchmark General Language Understanding Evaluation benchmark (GLUE) compara a performance de NLPMs
- Foi criado o benchmark SuperGLUE, que contém tarefas mais complicadas que o GLUE
- Os autores deste artigo criaram um benchmark para medir o conhecimento adquirido durante o pré-treino enquanto o avaliam em "zero-shot and few-shot settings"
- Este referido benchmark cobre 57 assuntos de STEM ("science, technology, engineering and mathematics"), humanidades, ciências sociais, ... Além disso, os problemas estão divididos em 3 níveis de dificuldade

##### Trabalho relacionado

- A avaliação dos NLP deve focar-se em NLG (Natural Language Generation) 
- NLG é dificil de avaliar e não tem uma métrica standard
- A avaliação passa pela medição da accuracy em perguntas de escolha múltipla (4 opções)


##### A multitask test

- Este teste consiste num conjunto de perguntas de escolha múltipla de vários ramos
- Dificuldades dos testes: "Elementary", "High School","College" e "Professional"
- Foram usados conjuntos de teste, validação e treino

##### Experiências
###### Setup
- Modelos usados do GPT-3:
    - GPT-3 Small (few-shot) - Ada
    - GPT-3 Medium (few-shot) - Babbage
    - GPT-3 Large (few-shot) - Curie
    - GPT-3 X-Large (few-shot) - Davinci
- Outros modelos usados:
    - Random Baseline
    - RoBERTa
    - ALBERT
    - GPT-2
    - UnifiedQA

##### Resultados
- Ver gráficos

##### Discussão

- Este benchmark só se baseia em testes apenas no formato de texto - será boa ideia extendê-los para imagens, audio, ...
- Este benchmark assume que os modelos já estão treinados com a informação que encontraram na internet
- Estes modelos ainda têm baixa performance comparativamente com a performance que pode ser alcançada pelos humanos
