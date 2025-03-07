import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

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
        # print(f"Erro ao corrigir o valor {valor}: {e}")
        return valor  # Retorna o valor original em caso de erro

def corrigir_loc_csv(input_csv, output_csv):
    """
    Corrige as colunas 'latitude' e 'longitude' em um arquivo CSV
    e salva as alterações em um novo arquivo.
    
    :param input_csv: Caminho do arquivo CSV de entrada.
    :param output_csv: Caminho do arquivo CSV corrigido de saída.
    """
    try:
        try:
            # Carrega o arquivo CSV
            df = pd.read_csv(input_csv)
        except:
            df = pd.read_csv(input_csv, encoding='latin1')

        for coluna in df.columns:
            if 'latitude' in coluna.lower():
                df.rename(columns={coluna: 'latitude'}, inplace=True)
            if 'longitude' in coluna.lower():
                df.rename(columns={coluna: 'longitude'}, inplace=True)
                        
        # Verifica e corrige as colunas de latitude e longitude
        if 'latitude' in df.columns and 'longitude' in df.columns:
            df['latitude'] = df['latitude'].apply(corrigir_lat_lon)
            df['longitude'] = df['longitude'].apply(corrigir_lat_lon)
        else:
            print("As colunas 'latitude' e 'longitude' não foram encontradas no arquivo.")
            return

        # Salva o novo arquivo corrigido
        df.to_csv(output_csv, index=False)
        print(f"Arquivo corrigido salvo como '{output_csv}'.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")



def verificar_localizacao(latitude, longitude, municipio):
    # Inicializa o geolocalizador
    geolocator = Nominatim(user_agent="verificador_localizacao")
    
    try:
        # Obtém o endereço correspondente à latitude e longitude
        location = geolocator.reverse((latitude, longitude), language='pt')
        if not location:
            return "Não foi possível determinar a localização para as coordenadas fornecidas."
        
        # Extrai o município do endereço
        endereco = location.raw.get('address', {})
        municipio_encontrado = endereco.get('city') or endereco.get('town') or endereco.get('village')
        
        # Compara com o município fornecido
        if municipio_encontrado and municipio_encontrado.lower() == municipio.lower():
            return f"As coordenadas correspondem ao município {municipio}."
        else:
            return f"As coordenadas não correspondem ao município {municipio}. Município encontrado: {municipio_encontrado}."
    
    except GeocoderTimedOut:
        return "O serviço de geolocalização demorou muito para responder. Tente novamente."