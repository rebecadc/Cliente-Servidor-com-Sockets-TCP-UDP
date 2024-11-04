import socket

def iniciar_cliente():
    protocolo = input("Escolha um protocolo (TCP/UDP): ").upper()
    mensagem = input("Digite a mensagem: ")
    
    if protocolo == "TCP":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
            tcp_socket.connect(("localhost", 5000))
            tcp_socket.send(mensagem.encode())
            resposta = tcp_socket.recv(1024).decode()
            print(f"Resposta do servidor: {resposta}")
    
    elif protocolo == "UDP":
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
            udp_socket.sendto(mensagem.encode(), ("localhost", 5001))
            resposta, _ = udp_socket.recvfrom(1024)
            print(f"Resposta do servidor: {resposta.decode()}")
    
    else:
        print("Protocolo inválido. Escolha TCP ou UDP.")

if __name__ == "__main__":
    iniciar_cliente()
