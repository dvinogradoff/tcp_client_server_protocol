"""
Тестовый-echo сервер
Использующий базовую библиотеку socket
"""
import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8888))
sock.listen(1)
conn, addr = sock.accept()

print('Соединение установлено:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    request = data.decode('utf-8')
    response = request
    print(f'Получен запрос: {ascii(request)}')
    print(f'Отправлен ответ {ascii(response)}')
    conn.sendall(response)

conn.close()
