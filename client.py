import socket
import threading

server_name = 'localhost'
port = 12345

user_name = input('введите имя: ')
# Создаем клиентский сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_name, port))  # Подключаемся к серверу

# Функция для отправки сообщений серверу
def send_message():
    while True:
        message = f'{user_name}: {input()}'
        client_socket.send(message.encode('utf-8'))

# Функция для приема сообщений от сервера
def receive_message():
    while True:
        try:
            message = client_socket.recv(1024)
            print(message.decode('utf-8'))
        except:
            print("Ошибка приема сообщения")
            break

# Создаем отдельные потоки для отправки и приема сообщений
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()