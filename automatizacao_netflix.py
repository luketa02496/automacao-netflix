import time
import os
import threading
import pyautogui
from datetime import datetime
from tkinter import Tk, filedialog

def programar_desligamento(): #* funcao usada para definir o horario de desligamento do PC
    while True:   
        
        hora = input("Informe a hora que voce deseja desligar o computador no formato: 0000. Relogio no formato 24h. \n-")

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
                
            confirma_hora=input(f"Confirmar hora de desligar? (S/N)\n {hora_desligar}h \n-").lower() 
                
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

    global hora_desligar
    global quer_desligar
    
    while True:
    
        acao = input("Qual ação voce deseja realizar? \n1- Programar ou reprogramar o desligamento. \n2- Cancelar o desligamento. \n3- Para encerrar o programa \n4- Para cancelar ação. \n-") #pergunta a acao

        if acao != "1" and acao != "2" and acao != "3" and acao != "4": # valida a resposta
            print("Resposta invalida! Tente novamente.")
            continue

        elif acao == "1": #se (1), programa o desligamento
            hora_desligar = programar_desligamento()
            quer_desligar = "s"
        
        elif acao == "3": #encerra o programa(3)
            print("Encerrando o programa...")
            exit() 
            

        elif acao == "4": #cancela a acao de repogramar o desligamento e retorna ao programa (4)
            print("Ação cancelada. Retornando ao programa...")
              
        else: #caso nao(2), desliga a programacao
            quer_desligar = "n"
            print("Desligamento do computador cancelado! \nRetornando ao programa...")
        
        break
        
def quer_reprogramar(): #* funcao deixada em segundo plano (thread) para capturar o input do usuario

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

root = Tk()
root.withdraw() 

#* bloco de codigo que pede o caminho das imagens e escreve em um arquivo de texto para usar depois
if os.path.exists('caminho_imagens.txt'): # verifica se o arquivo com o caminho das imagens existe
    
    with open('caminho_imagens.txt', "r", encoding= "utf-8") as arquivo: #le o arquivo de texto
        linhas = arquivo.readlines() #coloca a conteudo dentro da variavel

    pular_intro = linhas[0].strip() #coloca o conteudo dentro de variaveis separadas e remove o \n
    pular_ep = linhas[1].strip() 
    pular_recap = linhas[2].strip()

else:
    #TODO fazer a verificacao se foi selecionado alguma imagem
    imagens = []
    
    print("Selecione a imagem do botão 'pular intro'")
    pular_intro = filedialog.askopenfilename(title= "Selecione a imagem do botão 'pular intro'") # pede o caminho para a imagem
    imagens.append(pular_intro) #salva na lista

    print("Selecione a imagem do botão 'pular episodio'")
    pular_ep = filedialog.askopenfilename(title= "Selecione a imagem do botão 'pular episodio'")
    imagens.append(pular_ep)

    print("Selecione a imagem do botão 'pular recaptulação'")
    pular_recap = filedialog.askopenfilename(title= "Selecione a imagem do botão 'pular recaptulação'")
    imagens.append(pular_recap)

    with open('caminho_imagens.txt', "w", encoding = "utf-8") as arquivo: # cria o arquivo e coloca o caminho la dentro
        for imagem in imagens:
            print(imagem, file=arquivo)
    
    print("Arquivo de texto contendo o caminho para as imagens criado na mesma pasta do programa!\nNAO O CONTEUDO DESSE ARQUIVO")


#* declaracao de variaveis globais
resposta = None # variavel usada na funcao quer_reprogramar() para capturar qualquer input do usuario
contador = 12 # contador para o primeiro print

preparado = input('Abra a Netflix e pressione "Enter" quando estiver pronto!\n') #input que espera a confirmacao do usuario para iniciar o programa
print("Iniciando programa...")

t = threading.Thread(target=quer_reprogramar) #thread com funcao quer_reprogramar() para capturar o input do usuario e entrar na funcao reprogramar_desligamento()
t.start()

while True: #* loop principal
    
    if contador == 24: # a cada 24 voltas (2 minuto) no loop o print aparecera na tela
        print('Para cancelar o desligamento, trocar a hora do desligamento, programar para desligar ou encerrar o programa digite qualquer coisa ou aperter "Enter".') 
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
        botao2 = pyautogui.locateCenterOnScreen(pular_ep, confidence = 0.65)
        if botao2:
            pyautogui.click(botao2)
            time.sleep(1) 
            print("pulei episodio")

    except:
        pass
        
    try:
        #pular recap
        botao3 = pyautogui.locateCenterOnScreen(pular_recap, confidence = 0.65)
        if botao3:
            pyautogui.click(botao3)
            time.sleep(1) 
            print("pulei recap")
        
    except:
        pass

    contador+=1
    time.sleep(5)

#! MARCELLA EU TE AMOOOOOOOOOOOOOO MUITOOOOOOOOOOOOOOOOOOOOOOO<3