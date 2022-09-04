import requests
import shutil
import os

zpl = input('Insira o arquivo ZPL: ') #O usuário insere o arquivo ZPL.
url = "http://api.labelary.com/v1/printers/8dpmm/labels/4x6/0/^xa^cfa,50^fo100,100^fdHello World^fs^xz"
files = {'file' : zpl}
headers = {'Accept' : 'application/pdf'}
response = requests.post(url, headers = headers, files = files, stream = True)

if response.status_code == 200:
    response.raw.decode_content = True
    with open('Etiqueta.pdf', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
else:
    print('Error: ' + response.text)
#Até essa etapa, o progama já converteu o arquivo ZPL em PDF e já salvou na sua máquina.
os.startfile('Etiqueta.pdf') #Nesta etapa é inserido o nome do PDF e assim o programa conseguirá abrir.