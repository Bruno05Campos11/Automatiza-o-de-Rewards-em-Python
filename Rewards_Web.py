import pyautogui as pa
import time
from Mensagem import EnviarMensagem
pa.PAUSE = 1

pa.click (x=1335, y=59)
time.sleep (2)
pa.write ('edge')
pa.press ('ENTER')

#Rewards de Pesquisa
time.sleep (6)
pa.hotkey ("ctrl", "t")
time.sleep (6)
pa.write ("https://www.palavrasaleatorias.com/index.php")
pa.press ('ENTER')
time.sleep (6)

x = 0
while x < 30:
    pa.click (x=624, y=546)
    pa.click (clicks = 2, interval = 0.25, x=621, y=275)
    pa.hotkey ("ctrl", "c")
    pa.hotkey ("ctrl", "t")
    time.sleep (6)
    pa.hotkey ("ctrl", "v")
    pa.press ('ENTER')
    time.sleep (6)
    pa.hotkey ("ctrl", "w")
    x += 1

#Rewards no site
pa.click (x=22, y=18)
pa.click (x=110, y=228)
time.sleep (6)
pa.click (x=468, y=510)

time.sleep (6)
pa.click (x=0, y=500)
x = 0
while x < 10:
    pa.press ('down')
    x += 1

pa.click (x=339, y=620)
time.sleep (6)
pa.hotkey ("ctrl", "w")

pa.click (x=764, y=629)
time.sleep (6)
pa.hotkey ("ctrl", "w")

pa.click (x=1049, y=627)
time.sleep (6)
pa.hotkey ("ctrl", "w")

#Fechar Edge
pa.hotkey ("alt", "f4")

#Enviar Mensagem de conclusão para o WhatsApp
EnviarMensagem ("web")