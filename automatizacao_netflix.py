import pyautogui
import time
import os
from datetime import datetime

pular_intro = r"D:\dfotos\skip_intro.png"
pular_episodio = r"D:\dfotos\skip_episode.png"
pular_recap = r"D:\dfotos\skip_recap.png"

hora_desligar="02:00" #set a hora pra desligar

while True:
    agora = datetime.now().strftime("%H:%M") #pega a hora atual e formata para hora:minutos

    if agora == hora_desligar:
        os.system("shutdown /s /f /t 0") #desliga o pc. /s para desligar, /f para forcar parada dos aplicativos e /t tempo 0 segundos (instantaneo)

    try:
        #pular abertura
        botao = pyautogui.locateCenterOnScreen(pular_intro, confidence=0.8) #localiza o botao na tela
        if botao:
            pyautogui.click(botao) #clica no botao
            time.sleep(1) #espera 1 segundo
            print("pulei abertura")

    except:
        pass
    
    try:
        #pular episodio
        botao2 = pyautogui.locateCenterOnScreen(pular_episodio, confidence=0.6)
        if botao2:
            pyautogui.click(botao2)
            time.sleep(1) 
            print("pulei episodio")

    except:
        pass
        
    try:
        #pular recap
        botao3 = pyautogui.locateCenterOnScreen(pular_recap, confidence=0.6)
        if botao3:
            pyautogui.click(botao3)
            time.sleep(1) 
            print("pulei recap")
        
    except:
        pass

    time.sleep(5)  

