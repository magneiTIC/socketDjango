import socket
import select 

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host="127.0.0.1"
port=4000
serveur.listen(5)
try:
    serveur.bind((host, port))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.") 

print("Bienvenue dans le chat")

client,ip =serveur.accept();

while True:
    requeteClient=client.recv(500)
    requeteClient=requeteClient.decode("utf-8")
    print(requeteClient)
    if not requeteClient:
        print('close')
        break
    msg=input ('->')
    msg= msg.decode('utf-8')
    client.send(msg)

client.close()
socket.close()
