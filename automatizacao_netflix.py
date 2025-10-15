import time
import os
import threading
import pyautogui
import sys
from pathlib import Path
from datetime import datetime

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
                
            confirma_hora=input(f"Confirmar hora de desligar? (S/N)\n{hora_desligar}h \n-").lower() 
                
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
        os.system("shutdown /s /f /t 5") # desliga o pc. /s para desligar, /f para forcar parada dos aplicativos e /t tempo de 5 segundos 


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

def obter_caminhos_imagens(idioma): #* funcao usada para encontrar o caminho das imagens automaticamente sem que o usuario precise mexer
    
    if getattr(sys, 'frozen', False): #* verifica se o programa esta rodando em um .exe ou .py. o atributo sys.frozen so existe se o programa for empacotado (.exe). o if esta testando o resultado retornado por getattr(). entao se o atributo frozen existir (true) quer dizer que o script esta sendo executado por um .exe   
        base_dir = Path(sys._MEIPASS)  #se 'frozen' == true (.exe). coloca na variavel 'base_dir' o caminho temporario criado pelo arquivo .exe                        
                                                                                                                                    
    else:
        base_dir = Path(__file__).resolve().parent  #* se 'frozen' == false (.py). coloca na variavel o caminho do arquivo .py. Path(__file__) cria um Path para esse arquivo .py. .resolve() transforma em caminho absoluto e resolve links simbólicos. .parent retorna a pasta que contém o arquivo.

    pasta_imagens = base_dir / "imagens" #pega o caminho que esta o arquivo e soma com / para encontrar a pasta 'imagens'


    # define os caminhos dentro da pasta 'imagens'
    if idioma == "1": #portugues
        pular_intro = pasta_imagens / "pular_intro.png"
        pular_ep = pasta_imagens / "pular_ep.png"
        pular_recap = pasta_imagens / "pular_recap.png"
        
    elif idioma == "2": #ingles
        pular_intro = pasta_imagens / "skip_intro.png" 
        pular_ep = pasta_imagens / "next_ep.png"
        pular_recap = pasta_imagens / "skip_recap.png"

    # verifica se as imagens existem
    for img in [pular_intro, pular_ep, pular_recap]:
        if not img.exists():
            print("ERRO: uma ou mais imagens nao foram encontradas na pasta 'imagens'.")
            print("Certifique-se de que a pasta 'imagens' está junto do executável e/ou se todas as imagens se encontram dentro da pasta 'imagens'.")
            print("Encerrando o programa...")
            input("Pressione qualquer tecla para sair")
            sys.exit()

    return str(pular_intro), str(pular_ep), str(pular_recap) #retorna uma tupla de strings contendo o caminho para cada imagem e converte 'Path' para 'str'

def idioma_usuario(): #* funcao responsavel por perguntar ao usuario o idioma de sua netflix e salva em um arquivo txt

    while True: 
        idioma = input("Qual o idioma da sua Netflix? \n1- Portugues \n2- Ingles \n-")

        if idioma != "1" and idioma != "2": #valida a entrada
            print("Valor informado invalido! Apenas 1 ou 2. Tente novamente.")
            continue
        
        break

    with open('idioma.txt', "w", encoding="utf-8") as arquivo: #cria o arquivo e coloca salva dentro o idioma
        print(idioma, file=arquivo)
    
    print("Idioma salvo com sucesso!")
    return idioma

#!---------------------------------------------------------------------------- M A I N --------------------------------------------------------------------------------------------------------------------

while True: #* loop para perguntar se desejamos programar o desligamento do pc
    quer_desligar = input("Voce deseja programar o PC para desligar? (S/N) \n-").lower() #pergunta se quer desligar o PC e formata para lower case

    if quer_desligar != "s" and quer_desligar != "n": #verifica se foi uma resposta valida. S ou N
        print("Valor informado incorreto. Apenas (S/N). Tente novamente.")
        continue

    elif quer_desligar == "s": #se sim, chama a funcao para programar a hora de desligar
        hora_desligar = programar_desligamento()

    break


if not os.path.exists('idioma.txt'): #* verifica se o arquivo ja existe
    idioma = idioma_usuario()

else: # se o arquivo ja existir
    with open('idioma.txt', "r", encoding="utf-8") as arquivo: #le o arquivo
        idioma = arquivo.read().strip()
    
    if idioma == "1": #portugues
        idioma_formatado = "Portugues"

    else: #ingles
        idioma_formatado = "Ingles" 
            
    while True: #loop para confirmar o idioma salvo
        idioma_correto= input(f'O idioma salvo é: {idioma_formatado}. Deseja continuar(1) ou trocar de idioma(2)? \n-')

        if idioma_correto != "1" and idioma_correto != "2":
            print("Valor informado invalido! Apenas 1 ou 2. Tente novamente")
            continue

        break

    if idioma_correto == "2": #se deseja trocar de idioma
        idioma_usuario()


pular_intro, pular_ep, pular_recap = obter_caminhos_imagens(idioma) #configura o caminho para as imagens


#* declaracao de variaveis globais
resposta = None # variavel usada na funcao quer_reprogramar() para capturar qualquer input do usuario
contador = 60 # contador para o primeiro print

input('Abra a Netflix e pressione "Enter" quando estiver pronto!\n') #input que espera a confirmacao do usuario para iniciar o programa
print("Iniciando programa...")

t = threading.Thread(target=quer_reprogramar) #thread com funcao quer_reprogramar() para capturar o input do usuario e entrar na funcao reprogramar_desligamento()
t.start()

while True: #* loop principal
    
    if contador == 60: # a cada 60 voltas (5 minutos) no loop o print aparecera na tela
        print('Para cancelar o desligamento, alterar a hora do desligamento, programar para desligar, encerrar ou pausar o programa digite qualquer coisa ou pressione "Enter".') 
        contador = 0
    
    if resposta or resposta == "": # verifica a resposta da thread
        reprogramar_desligamento()
        resposta = None # reinicia a variavel para nulo       

        t = threading.Thread(target=quer_reprogramar) # inicia a thread novamente
        t.start()

    if quer_desligar == "s": 
        desligar_pc(hora_desligar) 

    try:
        #* pular abertura
        botao = pyautogui.locateCenterOnScreen(pular_intro, confidence = 0.8) #localiza o botao na tela com uma confianca de 80%
        if botao:
            pyautogui.click(botao) #clica no botao
            time.sleep(1) #espera 1 segundo
            print("pulei abertura")

    except:
        pass
    
    try:
        #* pular episodio
        botao2 = pyautogui.locateCenterOnScreen(pular_ep, confidence = 0.65)
        if botao2:
            pyautogui.click(botao2)
            time.sleep(1) 
            print("pulei episodio")

    except:
        pass
        
    try:
        #* pular recap
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

#TODO fazer um historico com todas as vezes que alguma açao foi feita 