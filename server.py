import socket
import threading

def handle_client(conn, addr):
    print(f"Conectado por {addr}")
    while True:
        try:
            mensagem = conn.recv(1024).decode()
            print(f"Recebido: {mensagem} pelo cliente {addr}")
            
            if mensagem == "Encerrar":
                resposta = "Encerrando serviço"
                conn.sendall(resposta.encode())
                break
            
            resposta = f"Comando '{mensagem}' executado no servidor \n Serviço prestado pela thread {threading.current_thread().name}"
            conn.sendall(resposta.encode())

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            break

    conn.close()
    print(f"{addr} Encerrou a conexão")

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 12345))
    servidor.listen()
    print("Servidor ouvindo na porta 12345...")

    while True:
        conn, addr = servidor.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
