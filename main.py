from LimpezaDeDados import corrigir_loc_csv, verificar_localizacao
import os

Pasta = 'Bancos/'
Saida = 'Data/'

# Iterar por todos os arquivos da pasta
for arquivo in os.listdir(Pasta):
    if arquivo.endswith('.csv'):
        input_csv = os.path.join(Pasta, arquivo)
        output_csv = os.path.join(Saida, 'corrigido_' + arquivo)
        corrigir_loc_csv(input_csv, output_csv)

        print(f"Arquivo '{arquivo}' corrigido com sucesso.")
        # print(f"Verificando localizações no arquivo '{output_csv}'...")
        
        # # Carregar o arquivo corrigido
        # df = pd.read_csv(output_csv, delimiter=';')
        
        # # Verificar localizações
        # for index, row in df.iterrows():
        #     latitude = row['latitude']
        #     longitude = row['longitude']
        #     municipio = row['municipio']
        #     resultado = verificar_localizacao(latitude, longitude, municipio)
        #     print(f"Registro {index}: {resultado}")
        
        # print()  # Adiciona uma linha em branco entre os arquivos
