import socket

def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr(ascii_offset + (25 - (ord(char) - ascii_offset)))
        else:
            result += char
    return result

def start_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('10.0.0.62', 12345))
        server_socket.listen(1)
        print("Server is listening...")

        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        
        message = client_socket.recv(1024).decode()
        print("Encrypted message received:", message)
        
        decrypted_message = atbash_cipher(message)
        print("Decrypted message:", decrypted_message)
        
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    start_server()