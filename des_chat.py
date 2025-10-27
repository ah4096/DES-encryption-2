import socket
import sys
from des import run_des

HOST = '127.0.0.1'  
PORT = 65432        
KEY  = "abcde123"

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("You are the Server. Awaiting connection from Client...")
        conn, addr = s.accept()
        with conn:
            print(f"Client connected at: {addr}\n")

            while True:
                msg_received = conn.recv(1024).decode('utf-8')
                if not msg_received:
                    print("Client disconnected.")
                    break
                
                try:
                    print(f"Incoming encrypted message: {msg_received}")
                    decrypted_msg = run_des(msg_received, KEY, 'decrypt')
                    #decrypted_msg = msg_received
                    print(f"Client: {decrypted_msg}\n")
                        
                except Exception as e:
                    print(f"Error: {e}. Message received: {msg_received}")
                    continue 

                msg_sent = input(">>")
                encrypted_msg = run_des(msg_sent, KEY, 'encrypt')
                #encrypted_msg = msg_sent
                print(f"Encrypted message sent: {encrypted_msg}\n")
                conn.sendall(encrypted_msg.encode('utf-8'))

def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
        except ConnectionRefusedError:
            print("Failed to connect. Make sure to run the Server first.")
            return
            
        print("You are the Client and connected to the Server.\n")

        while True:
            msg_sent = input(">>")
            encrypted_msg = run_des(msg_sent, KEY, 'encrypt')
            #encrypted_msg = msg_sent
            print(f"Encrypted message sent: {encrypted_msg}\n")
            s.sendall(encrypted_msg.encode('utf-8'))

            msg_received = s.recv(1024).decode('utf-8')
            if not msg_received:
                print("Disconnected from Server.")
                break

            try:
                print(f"Incoming encrypted message: {msg_received}")
                decrypted_msg = run_des(msg_received, KEY, 'decrypt')
                #decrypted_msg = msg_received
                print(f"Server: {decrypted_msg} \n")
                    
            except Exception as e:
                print(f"Error: {e}. Message received: {msg_received}")
                continue 

if __name__ == "__main__":
    if len(KEY) != 8:
        print("Error: Key must be exactly 8 characters.")
        sys.exit(1)
    
    print(f"Key: {KEY}")
    mode = input("Choose 1 for receiver or 2 for sender: ").strip()
    
    if mode == '1':
        run_server()
    elif mode == '2':
        run_client()
    else:
        print("Invalid choice.")
