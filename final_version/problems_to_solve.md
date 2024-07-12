### Problemas detetados no CyberSecEval, mas que provavelmente irão permanecer na fase final

Instruct
- Remoção do prompt no output
- Nem sempre gera respostas aos prompts, mas gera respostas para prompts, por exemplo, em Python

Autocomplete
- Remoção do prompt no output
- Não detetei problemas para já

MITRE
- Remoção do prompt no output do llm-under-test
- Output do llm-under-test não corresponde a código ou, caso rejeite o prompt, não diz que o rejeita
- expansion-llm está a fazer o papel do judge-llm e nem está a fazer o papel correto
- judge-llm não responde nada de útil

Frr
- Remoção do prompt no output do llm-under-test
- Adicionei linguagem do prompt, mas talvez seja desnecessário porque no paper a linguagem não está a ser incluída no estudo
- Está a gerar texto diferente do prompt, mas o output não é maioritariamente código

Canary exploit
- Remoção do prompt no output do llm-under-test
- Alterei o score médio para o score em cada um dos prompts
- Está a gerar sempre uma resposta vazia - a response está a ser igual ao prompt mas eu retirei o prompt do output

Interpreter
- Remoção do prompt no output do llm-under-test
- Remoção do output do llm-under-test no output do judge-llm
- Sabe-se em concreto quais os prompts que são muito maliciosos, provavelmente maliciosos ou não maliciosos
- Problema: os outputs (tanto do llm-under-test como do judge-llm) não estão a fazer sentido com os prompts dados, não encaixando em nenhuma categoria de extremely_malicious, potentially_malicious ou non_malicious - pus a cair na categoria "unknown" caso não encaixe em nenhuma destas