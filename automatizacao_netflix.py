import time
import os
import threading
import pyautogui
from datetime import datetime

def programar_desligamento(): #* funcao usada para definir o horario de desligamento do PC
    while True:   
        
        hora = input("Informe a hora que voce deseja desligar o computador. Formato: 0000. \n-")

        if not hora.isdigit(): #verifica se é um numero
            print ("Caracteres informados invalidos! \nTente novamente.")
            continue

        elif len(hora) !=4 : #verifica o tamanho
            print("Tamanho invalido! Informe apenas 4 numeros! \nTente novamente.")
            continue
        
        elif int(hora[2:]) >=60 or int(hora[:2]) >=25: #verifica se sao horas e minutos validos
            print("A hora não deve ser maior que 24 e os minutos não devem passar de 59! \nTente novamente.")
            continue
        
        hora_desligar = hora[:2] + ":" + hora[2:] #adiciona : entre as horas e os minutos
        while True:
                
            confirma_hora=input(f"Confirmar hora de desligar? (S/N)\n {hora_desligar} \n-").lower() 
                
            if confirma_hora != "s" and confirma_hora != "n": #verifica a resposta
                print("Valor informado incorreto. Apenas (S/N).")
                continue
                    
            break
                
        if confirma_hora == "s": # se sim, set a hora para desligar e sai do loop
            print(f"Computador programado para desligar as: {hora_desligar}h")
            break

        print("Retornando...") #caso nao, retorna para o comeco do loop
              
    return hora_desligar # retorna a hora para desligar


def desligar_pc(hora_desligar): #* funcao usada para verificar a hora do computador e desligar na hora programada

    agora = datetime.now().strftime("%H:%M") #pega a hora atual e formata para hora:minutos

    if agora == hora_desligar:
        os.system("shutdown /s /f /t 0") # desliga o pc. /s para desligar, /f para forcar parada dos aplicativos e /t tempo de 0 segundos (instantaneo)


def reprogramar_desligamento(): #* funcao usada para reprogramar o desligamento do pc
    while True:
        global hora_desligar
        global quer_desligar
        global var_controle

        acao = input("Qual ação voce deseja realizar? \n1- Programar ou reprogramar o desligamento. \n2- Cancelar o desligamento. \n3- Para encerrar o programa \n4- Para cancelar ação. \n-") #pergunta a acao

        if acao != "1" and acao != "2" and acao != "3" and acao != "4": # valida a resposta
            print("Resposta invalida! Tente novamente.")
            continue

        elif acao == "1": #se sim(1), programa o desligamento
            hora_desligar = programar_desligamento()
            quer_desligar = "s"
        
        elif acao == "3": #encerra o programa(3)
            var_controle = 1
            print("Encerrando o programa...")

        elif acao == "4": #cancela a acao de repogramar o desligamento e retorna ao programa
            print("Ação cancelada. Retornando ao programa...")
              
        else: #caso nao(2), desliga a programacao
            quer_desligar = "n"
            print("Desligamento do computador cancelado! \nRetornando ao programa...")
        
        break
        
def quer_reprogramar(): #* funcao deixada em segundo plano para receber a resposta 

    global resposta
    resposta = input()


#!---------------------------------------------------------------------------- M A I N --------------------------------------------------------------------------------------------------------------------


while True: #* loop para perguntar se desejamos programar o desligamento do pc
    quer_desligar = input("Voce deseja programar o PC para desligar? (S/N) \n-").lower() #pergunta se quer desligar o PC e formata para lower case

    if quer_desligar != "s" and quer_desligar != "n": #verifica se foi uma resposta valida. S ou N
        print("Valor informado incorreto. Apenas (S/N). Tente novamente.")
        continue

    elif quer_desligar == "s": #se sim, chama a funcao para programar a hora de desligar
        hora_desligar = programar_desligamento()

    break

t = threading.Thread(target=quer_reprogramar) #thread com o input
t.start()

#* declaracao de variaveis globais
resposta = None # variavel usada na funcao quer_reprogramar() para capturar qualquer input do usuario
var_controle = 2 # inicia o loop
contador = 12 # contador para o primeiro print

#* caminho para as imagens usadas no pyautogui
pular_intro = r"D:\dfotos\skip_intro.png"
pular_episodio = r"D:\dfotos\next_ep.png"
pular_recap = r"D:\dfotos\skip_recap.png"

while var_controle !=1: #* loop principal
    
    if contador == 12: # a cada 12 voltas (1 minuto) no loop o print aparecera na tela
        print('Para cancelar o desligamento, trocar a hora, programar para desligar ou encerrar o programa digite qualquer coisa ou aperter "Enter".') 
        contador = 0
    
    if resposta or resposta == "": # verifica a resposta da thread
        reprogramar_desligamento()
        resposta = None # reinicia a variavel para nulo

        t = threading.Thread(target=quer_reprogramar) # inicia a thread novamente
        t.start()

    if quer_desligar == "s":
        desligar_pc(hora_desligar) 

    try:
        #pular abertura
        botao = pyautogui.locateCenterOnScreen(pular_intro, confidence = 0.8) #localiza o botao na tela com uma confianca de 80%
        if botao:
            pyautogui.click(botao) #clica no botao
            time.sleep(1) #espera 1 segundo
            print("pulei abertura")

    except:
        pass
    
    try:
        #pular episodio
        botao2 = pyautogui.locateCenterOnScreen(pular_episodio, confidence = 0.8)
        if botao2:
            pyautogui.click(botao2)
            time.sleep(1) 
            print("pulei episodio")

    except:
        pass
        
    try:
        #pular recap
        botao3 = pyautogui.locateCenterOnScreen(pular_recap, confidence = 0.8)
        if botao3:
            pyautogui.click(botao3)
            time.sleep(1) 
            print("pulei recap")
        
    except:
        pass

    contador+=1
    time.sleep(5)

print('Programa encerrado')

    



    



        



        


    

        

    
    
















