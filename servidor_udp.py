import socket

def iniciar_servidor_udp():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("localhost", 5001))
    print("Servidor UDP escutando na porta 5001...")
    
    while True:
        mensagem, endereço_cliente = udp_socket.recvfrom(1024)
        resposta = f"UDP: {mensagem.decode()}"
        udp_socket.sendto(resposta.encode(), endereço_cliente)

if __name__ == "__main__":
    iniciar_servidor_udp()