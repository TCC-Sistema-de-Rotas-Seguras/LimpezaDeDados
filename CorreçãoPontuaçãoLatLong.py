import pandas as pd

def corrigir_lat_lon(valor):
    """
    Remove todos os pontos de um número, 
    e insere um ponto após a segunda casa decimal.
    """
    try:
        valor_str = str(valor).replace('.', '')  # Remove todos os pontos
        if valor_str.startswith('-'):  # Preserva o sinal negativo
            sinal = '-'
            valor_str = valor_str[1:]
        else:
            sinal = ''
        # Coloca o ponto após a segunda casa decimal
        valor_corrigido = sinal + valor_str[:2] + '.' + valor_str[2:]
        return float(valor_corrigido)  # Converte de volta para número
    except Exception as e:
        print(f"Erro ao corrigir o valor {valor}: {e}")
        return valor  # Retorna o valor original em caso de erro

# Caminho do arquivo CSV
arquivo_csv = "./Dados/dados_limpos_Dados_Criminais_ABC_2022 (Formatado).csv"  # Substitua pelo nome do seu arquivo

# Carrega o arquivo CSV
df = pd.read_csv(arquivo_csv, delimiter=';')


# Corrige as colunas de latitude e longitude
if 'latitude' in df.columns and 'longitude' in df.columns:
    df['latitude'] = df['latitude'].apply(corrigir_lat_lon)
    df['longitude'] = df['longitude'].apply(corrigir_lat_lon)
else:
    print("As colunas 'latitude' e 'longitude' não foram encontradas no arquivo.")

# Salva as alterações em um novo arquivo CSV
novo_arquivo_csv = "arquivo_corrigido.csv"
df.to_csv(novo_arquivo_csv, index=False)
print(f"Arquivo corrigido salvo como '{novo_arquivo_csv}'.")
