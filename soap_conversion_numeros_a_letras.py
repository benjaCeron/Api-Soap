import zeep
import requests
import xml.etree.ElementTree as ET
from googletrans import Translator

def obtener_numero_del_usuario():
    while True:
        try:
            numero = int(input("Por favor, introduce el número que deseas convertir a palabras: "))
            return numero
        except ValueError:
            print("Por favor, introduce un número válido.")

def solicitud_soap(numero):
    # URL de la solicitud SOAP
    url = "https://www.dataaccess.com/webservicesserver/numberconversion.wso"

    # XML estructurado
    payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
                <soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
                    <soap:Body>
                        <NumberToWords xmlns=\"http://www.dataaccess.com/webservicesserver/\">
                            <ubiNum>{numero}</ubiNum>
                        </NumberToWords>
                    </soap:Body>
                </soap:Envelope>"""
    # Encabezados
    headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }
    # Solicitud POST
    response = requests.post(url, headers=headers, data=payload)

    # Imprimir la respuesta
    print("Respuesta XML:", response.text)
    print("Estado de la respuesta:", response)

    root = ET.fromstring(response.text)

    # Encontrar el elemento NumberToWordsResult
    resultado_numerico = root.find(".//{http://www.dataaccess.com/webservicesserver/}NumberToWordsResult")

    # Si se encontró el elemento, imprimir su texto
    if resultado_numerico is not None:
        return resultado_numerico.text.strip()
    else:
        print("Número no encontrado en la respuesta")
        return ""

def traducir_a_espanol(texto):
    translator = Translator()
    translation = translator.translate(texto, src='en', dest='es')
    return translation.text

def convertir_numero_a_palabras(numero):
    texto_en_ingles = solicitud_soap(numero)
    if texto_en_ingles:
        texto_en_espanol = traducir_a_espanol(texto_en_ingles)
        print("Número en palabras (en español):", texto_en_espanol)

if __name__ == "__main__":
    numero = obtener_numero_del_usuario()
    convertir_numero_a_palabras(numero)