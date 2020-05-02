import requests
import json
import hashlib

# Variáveis Primárias

url_codenation = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data"
token = ""

# 1. Requisição HTTP do site
reqHttp = requests.get(url_codenation, params={"token": token})
print("Código de Status: ", reqHttp.status_code)
if reqHttp.status_code == 200:
    print('Sucesso')
else:
    print("ERROR")
reqJson = json.loads(reqHttp.text)
# print(reqJson)

# print(r.json())
# print(r.url)
# print(r.content)

with open("answer.json", "w") as file:
    json.dump(reqJson, file, ensure_ascii=False, indent=4)

# 2. Decriptação

criptoRes = reqJson["cifrado"]
print("Mensagem criptografada:", criptoRes)
num_casas = reqJson["numero_casas"]
print("Deslocamento de letras:", num_casas)

message = ""

for char in criptoRes:
    if ord(char) >= 97 and ord(char) <= 122:  # Tabela ASCII de letras minusculas
        letter = (chr(ord(char) - num_casas))
        message = message[0:] + letter
    else:
        message = message[0:] + char

print(message)
decryptMessage = message



summary = hashlib.sha1(decryptMessage.encode()).hexdigest()
print(summary)

# 3. Envio da Requisição

reqJson['decifrado'] = decryptMessage
reqJson['resumo_criptografico'] = summary
print(reqJson)

with open("answer.json", "w") as file:
    json.dump(reqJson, file, ensure_ascii=False, indent=4)

answer = {"answer": open("answer.json", "rb")}
url_resultado = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution"

resultados = requests.post(url_resultado, files=answer, params={"token": token})
print(resultados.status_code)
print(resultados.text)


