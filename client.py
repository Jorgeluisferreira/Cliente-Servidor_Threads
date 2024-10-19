import socket
import time

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 12345))
    
    while True:
        mensagem = input("Digite sua mensagem (ou 'Encerrar' para sair): ")
        cliente.sendall(mensagem.encode())
        
        resposta = cliente.recv(1024).decode()
        print(f"Resposta do servidor: {resposta}")

        if mensagem == "Encerrar":
            break

    cliente.close()

if __name__ == "__main__":
    main()
