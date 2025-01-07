from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

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

# Exemplo de uso
latitude = float(input("Digite a latitude: "))
longitude = float(input("Digite a longitude: "))
municipio = input("Digite o nome do município: ")

resultado = verificar_localizacao(latitude, longitude, municipio)
print(resultado)
