# server.py
import random
from socket import *

def handle_received_client_message(message):
    message_parts = message.split('|')
    sentence = message_parts[0]
    status_code = int(message_parts[1])
    status_phrase = message_parts[2]
    print(f"Received from client Message: {sentence}, Status code: {status_code}, Status phrase: {status_phrase}")
    return sentence, status_code, status_phrase

def handle_send_client_message(sentence, status_code, status_phrase):
    full_message = f"{sentence}|{status_code}|{status_phrase}"
    return full_message

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print('The server is ready to receive')
category1 = ['Pizza','Burger','FriedChicken','Hotdog','Spaghetti','Steak','Salad','Sandwich','Sushi','Sashimi','Udon','Tempura','Tonkatsu','Yakitori','Yakiniku','Kimchi','Bibimbap','Bulgogi','Tteokbokki','Samgyeopsal','Japchae','Dakgalbi','Padthai','TomYumKung','Somtum','Krapao','KuayTiew','KhaoPad','Ramens','Sushi','Sashimi','Udon','Tempura','Tonkatsu','Yakitori','Yakiniku','Kimchi','Bibimbap','Bulgogi','Tteokbokki','Samgyeopsal','Japchae','Dakgalbi','Pizza','Burger','FriedChicken','Hotdog','Spaghetti','Steak','Salad','Sandwich','Sushi','Sashimi','Udon','Tempura','Tonkatsu','Yakitori','Yakiniku','Kimchi','Bibimbap','Bulgogi','Tteokbokki','Samgyeopsal','Japchae','Dakgalbi','Padthai','TomYumKung','Somtum','Krapao','KuayTiew','KhaoPad','Ramens','Sushi','Sashimi','Udon','Tempura','Tonkatsu','Yakitori','Yakiniku','Kimchi','Bibimbap','Bulgogi','Tteokbokki']
category2 = ['Padthai','TomYumKung','Somtum','Krapao','KuayTiew','KhaoPad']
category3 = ['Ramens','Sushi','Sashimi','Udon','Tempura','Tonkatsu','Yakitori','Yakiniku']
category4 = ['Kimchi','Bibimbap','Bulgogi','Tteokbokki','Samgyeopsal','Japchae','Dakgalbi']
while True:
     connectionSocket, addr = serverSocket.accept()
     
     while True:
          message = connectionSocket.recv(1024).decode()

          sentence, status_code, status_phrase = handle_received_client_message(message)

          if sentence == 'exit':
               break
          if sentence == '1':
               ans = random.choice(category1)
          elif sentence == '2':
               ans = random.choice(category2)
          elif sentence == '3':
               ans = random.choice(category3)
          elif sentence == '4':
               ans = random.choice(category4)

          message = handle_send_client_message(ans, "200", "OK")
          connectionSocket.send(message.encode())
          print('Message sent to client', addr)
          print('-------------------------------------------------------------\n')
     connectionSocket.close()


