import socket
host="127.0.0.1"
port=4000 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((host, port))
except socket.error:
    print("La connexion a échoué.") 
print("Connexionétablieavecleserveur.")

while True:
    msg=input ('->')
    msg= msg.decode('utf-8')
    client.send(msg)

    requete_server=socket.recv(500)
    requete_server=requete_server.decode('utf-8')
    print(requete_server)
