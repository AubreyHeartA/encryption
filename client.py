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

def start_client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('10.0.0.62', 12345))
        
        message = input("Enter the message to send: ")
        encrypted_message = atbash_cipher(message)
        print("Encrypted message:", encrypted_message)
        
        client_socket.send(encrypted_message.encode())
        
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
