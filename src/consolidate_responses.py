import json
import glob
import pandas as pd

def load_data():
    # Carrega todos os arquivos JSON
    data_files = glob.glob("data/hour=*.json")
    data = []
    for file in data_files:
        with open(file, 'r') as f:
            data.extend(json.load(f))
    return data

def process_data(data):
    # Converte para DataFrame
    df = pd.json_normalize(data)

    # Identifica todas as colunas que começam com 'content.' para as respostas dos usuários
    content_columns = [col for col in df.columns if col.startswith("content.")]
    
    # Renomeia as colunas de conteúdo para remover o prefixo 'content.'
    df = df.rename(columns={col: col.replace("content.", "") for col in content_columns})

    # Ordena por timestamp para identificar as primeiras e últimas respostas
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by=['customer', 'flow', 'session', 'timestamp'])

    # Define a agregação para cada coluna de resposta como 'first'
    agg_dict = {col: 'first' for col in df.columns if col not in ['customer', 'flow', 'session', 'timestamp']}
    # Adiciona timestamp como 'first' e 'last' para as respostas
    agg_dict['timestamp'] = ['first', 'last']

    # Realiza o agrupamento e agregação
    result = df.groupby(['customer', 'flow', 'session']).agg(agg_dict)
    result.columns = ['first_answer_dt', 'last_answer_dt'] + [col for col in df.columns if col not in ['customer', 'flow', 'session', 'timestamp']]
    result = result.reset_index()

    return result

def main():
    pd.set_option('display.max_columns', None)  # Exibe todas as colunas
    pd.set_option('display.width', 1000)        # Ajusta a largura de exibição
    
    data = load_data()
    result = process_data(data)
    print(result)

if __name__ == "__main__":
    main()
