# Projeto Zenvia - Parte 3

Este projeto consolida as respostas de usuários de uma plataforma de chatbot, extraindo as primeiras e últimas respostas de cada sessão.

## Estrutura do Projeto

- `data/hour=13.json` e `data/hour=14.json`: Arquivos JSON com dados de respostas de usuários.
- `src/consolidate_responses.py`: Script que processa e consolida as respostas em um relatório.

## Como Executar

1. Instale as dependências necessárias:

   ```bash
   pip install pandas
   ```

2. Execute o script:

   ```bash
   python3 src/consolidate_responses.py
   ```

O script irá gerar um relatório consolidado exibindo a primeira e última interação de cada sessão de usuário.

  customer   flow session first_answer_dt  last_answer_dt   name        cpf delivery_confirmed           recomenda                nota
0    C1000  F1000   S1000           maria  305.584.960-40   true       None               None 2019-12-16 13:59:58 2019-12-16 13:59:58
1    C1000  F1000   S2000            joao  733.600.420-26  false       None               None 2019-12-16 13:59:59 2019-12-16 13:59:59
2    C2000  F2000   S3000            None            None   None  Simmmmmmm                  9 2019-12-16 14:00:01 2019-12-16 14:00:01