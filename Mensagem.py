import pyautogui as pa
import time

#Este código só funcionará caso tiver instalado no pc o WhatsApp

def EnviarMensagem (tipo):
    pa.click (x=1335, y=59)
    time.sleep (2)
    pa.write ('whatsapp')
    time.sleep (2)
    pa.press ('ENTER')

    time.sleep (15)
    pa.click (x=184, y=117)
    pa.write ('meu numero')
    time.sleep (4)
    pa.click (x=199, y=173)

    time.sleep (4)
    pa.click (x=628, y=731)
    
    if tipo == "pc": #No meu computador há automatização da Rewards de Pc, mas ela não funciona como desejado
        pa.write ("Rewards do Pc acabou aqui")
    elif tipo == "web":
        pa.write ("Concluído Rewards da Web")
        
    pa.press ('ENTER')
    time.sleep (10)
    pa.hotkey ("alt", "f4")
