import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8000
count = 0

print('Trying to connect...')
while count == 0:
    try:
        s.connect(("localhost", port))
        count += 1
    except:
        pass

print('You have connected successfully')

print('Check your personality...')
print('Enter a number between 0 to 1000...')


def listen():
    while True:
        data = s.recv(1024)
        print('Localhost>' + data.decode('utf-8'))


def send():
    while True:
        msg = input(">")
        s.sendall(msg.encode('utf-8'))


if __name__ == "__main__":
    threading.Thread(target=listen).start()
    threading.Thread(target=send).start()
