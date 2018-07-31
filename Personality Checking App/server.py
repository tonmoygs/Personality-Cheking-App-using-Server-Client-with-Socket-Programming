import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8000
s.bind(("", port))
s.listen(5)

print('Waiting for connection...')

client, addr = s.accept()

print('Client '+str(addr[0])+' has connected')


def send(data):
    data2 = 0

    try:
        data2 = int(data)
        if 0 <= data2 <= 1000:
            if data2 % 3 == 0 and '3' in data:
                client.sendall(b'Dumb')
            elif data2 % 3 == 0:
                client.sendall(b'Idiot')
            elif '3' in data:
                client.sendall(b'Stupid')
            else:
                client.sendall(b'Smart')
    except:
        client.sendall(b'invalid')


def listen():
    while True:
        data = client.recv(1024)
        print(str(addr[0])+'> ' + data.decode('utf-8'))
        data = data.decode('utf-8')
        if data is not None:
            send(data)


if __name__ == '__main__':
    threading.Thread(target=listen).start()
