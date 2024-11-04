import socket

def iniciar_servidor_tcp():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("localhost", 5000))
    tcp_socket.listen(5)
    print("Servidor TCP escutando na porta 5000...")

    while True:
        client_socket, endereço_cliente = tcp_socket.accept()
        message = client_socket.recv(1024).decode()
        response = f"TCP: {message}"
        client_socket.send(response.encode())
        client_socket.close()

if __name__ == "__main__":
    iniciar_servidor_tcp()
