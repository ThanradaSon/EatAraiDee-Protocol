#client.py
from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

def handle_received_server_message(message):
    message_parts = message.split('|')
    sentence = message_parts[0]
    status_code = int(message_parts[1])
    status_phrase = message_parts[2]
    print(f"Received from server Message: {sentence}, Status code: {status_code}, Status phrase: {status_phrase}")
    return sentence, status_code, status_phrase

print('Don\'t know what to eat? Let me help you!')
while True:
    print('Input number of category (If you want to exit type "exit")')
    print('1 Up to you Food')
    print('2 Thai Food')
    print('3 Japanese Food')
    print('4 Korean Food')

    sentence = input('Type Here: ')
    status_code = 200
    status_phrase = "OK"
    full_message = f"{sentence}|{status_code}|{status_phrase}"

    if sentence == 'exit':
        clientSocket.send(full_message.encode())
        print('Message sent to server')
        break

    clientSocket.send(full_message.encode())
    print('Message sent to server')
    ans_message = clientSocket.recv(1024)
    sentence, status_code, status_phrase = handle_received_server_message(ans_message.decode())
    print ('Here It is the menu:', sentence)
    print('-------------------------------------------------------------\n')

clientSocket.close()
