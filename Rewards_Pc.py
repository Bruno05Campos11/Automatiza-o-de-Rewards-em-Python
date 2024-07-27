import pyautogui as pa
import time
from Mensagem import EnviarMensagem

#Lembrar de deixar aberto na aba do jogo
x = 0
while x < 18:
    time.sleep (50)
    pa.click (x=428, y=234)
    x += 1

#fechar o jogo
pa.click (x=1104, y=84)
time.sleep (10)

#Enviar mensagem de conclusão para o WhatsApp
EnviarMensagem("pc")