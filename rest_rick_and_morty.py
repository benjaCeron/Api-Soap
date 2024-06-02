import requests


def obtener_personaje_por_id(id):
    # Define la URL del endpoint de la API
    url = f'https://rickandmortyapi.com/api/character/{id}'

    try:
        # Realiza una solicitud GET a la URL del endpoint usando requests.get()
        response = requests.get(url)

        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            personaje = response.json()
            return personaje
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:

        # Maneja cualquier error o excepción relacionados con la red
        print('Error:', e)
        return None

def solicitar_id_personaje():
    while True:
        try:
            id = int(input("Por favor, introduce el ID del personaje que deseas conocer: "))
            return id
        except ValueError:
            print("Por favor, introduce un ID válido.")

if __name__ == "__main__":
    id_personaje = solicitar_id_personaje()
    personaje = obtener_personaje_por_id(id_personaje)
    if personaje:
        print("Información del personaje:")
        print(f"Nombre: {personaje['name']}")
        print(f"Especie: {personaje['species']}")
        print(f"Estado: {personaje['status']}")
        print(f"Género: {personaje['gender']}")
    else:
        print("No se pudo obtener información del personaje.")
