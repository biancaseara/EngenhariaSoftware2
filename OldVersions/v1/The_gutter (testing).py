'''
Bibliotecas Usadas:
    Pygame
    Time
    Keyboard
    Colorama
'''
import os, colorama, pygame, time, keyboard
pygame.mixer.init()
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from pygame import mixer
os.system('cls')
import sys,time

#Configurações de operação
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(4./90)

def ssprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(6./90)

def editNome():
    os.system('cls')
    sprint(f'Então o seu nome é {"".join(User)}, correto?')
    name_choice = input('[1] SIM\n[2] NÃO\n>>> ')
    if name_choice == '2':
        newname = input('Corrija seu nome, por favor\n>>> ')
        User[0] = newname
        editNome()
    else:
        sprint('Ótimo.')
        input()

def editSigno():
    os.system('cls')
    print(Fore.RED + 'ANFITRIÃO')
    sprint(f'Então seu signo é {"".join(Signo)}, correto?')
    sign_choice = input('[1] SIM\n[2] NÃO\n>>> ')
    if sign_choice == '2':
        print(Fore.RED + 'ANFITRIÃO')
        sprint('Claro, podemos corrigir.')
        newsign = input('Informe seu signo correto:\n>>> ')
        Signo[0] = newsign
        editSigno()
    else:
        sprint('Perfeito.')
        input()
        os.system('cls')

def cleanup():
    EscolhaImpacto1.clear
    EscolhaImpacto2.clear
    EscolhaImpacto3.clear
    EscolhaQueimarArvore.clear
    EscolhaCriançaSalva.clear
    QTE_Tutorial.clear
    QTE_1.clear
    QTE_2.clear
    QTE_3.clear
    QTE_4.clear
    QTE_5.clear
    QTE_6.clear

def menu():
    while True:
        os.system('cls')
        #No caso de erro ao encontrar música, procurar localização na pasta que contém a música nos arquivos do jogo e alterar sua localização no código abaixo.
        pygame.mixer.music.load("menu_song.ogg")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()
        print(Style.BRIGHT + Fore.RED + Back.LIGHTWHITE_EX + '----- THE GUTTER -----')
        sprint('[1] Iniciar aventura (DEMO)')
        sprint('[0] Sair')
        menu_choice = input('>>> ')
        if menu_choice == '1':
            cleanup()
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.unload()
            introAnfitrião()
            inicio_demo()
        elif menu_choice == '0':
            print('Nos vemos em breve...')
            break

def new_menu():
    while True:
        os.system('cls')
        #No caso de erro ao encontrar música, procurar localização na pasta que contém a música nos arquivos do jogo e alterar sua localização no código abaixo.
        pygame.mixer.music.load("menu\music\menu_song.ogg")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()
        print(Style.BRIGHT + Fore.RED + Back.LIGHTWHITE_EX + '----- THE GUTTER -----')
        sprint('[1] Iniciar aventura (DEMO)')
        sprint('[2] Escolhas')
        sprint('[0] Sair')
        menu_choice = input('>>> ')
        if menu_choice == '1':
            cleanup()
            pygame.mixer.music.fadeout(1000)
            introAnfitrião()
            inicio_demo()
        elif menu_choice == '2':
            show_choices()
        elif menu_choice == '0':
            print('Nos vemos em breve...')
            break

def show_choices():
    os.system('cls')
    print(Fore.RED + Back.WHITE + '===== ESCOLHAS =====')
    print('')
    print('========================================================================')
    sprint(f'{EscolhaImpacto1}')
    print('========================================================================')
    sprint(f'{EscolhaImpacto2}')
    print('========================================================================')
    sprint(f'{EscolhaImpacto3}')
    print('========================================================================')
    sprint(f'{EscolhaQueimarArvore}')
    print('========================================================================')
    sprint(f'{EscolhaCriançaSalva}')
    print('========================================================================')
    input('[ENTER] para continuar...')

#Dados de jogo importantes
User = []
Signo = []
Planta = []
Inventario = []

#Escolhas
EscolhaImpacto1 = []
EscolhaImpacto2 = []
EscolhaImpacto3 = []
EscolhaQueimarArvore = []
EscolhaCriançaSalva = []

#QTE's

QTE_Tutorial = []

def qte_tutorial():
    print("Pressione a tecla 'A'!")
    time.sleep(2)  # Aguarda 2 segundos antes de começar

    start_time = time.time()  # Registra o tempo inicial

    while True:
        if keyboard.is_pressed('a'):  # Verifica se a tecla 'A' foi pressionada
            end_time = time.time()  # Registra o tempo em que a tecla foi pressionada
            reaction_time = end_time - start_time  # Calcula o tempo de reação
            if reaction_time < 2:
                print('SUCESSO!')
                QTE_Tutorial.append('SUCESSO')
            else:
                print('FALHA!')
                QTE_Tutorial.append('FALHA')
            print("Tempo de reação:", reaction_time)
            break  # Sai do loop

    print("Pressione a tecla 'G'!")
    time.sleep(2)

    start_time = time.time() 

    while True:
        if keyboard.is_pressed('g'):
            end_time = time.time() 
            reaction_time = end_time - start_time 
            if reaction_time < 1:
                print('SUCESSO!')
                QTE_6.append('SUCESSO')
            else:
                print('FALHA!')
                QTE_6.append('FALHA')
            print("Tempo de reação:", reaction_time)
            break

#Cenários

def introAnfitrião():
    os.system('cls')
    sprint('Olá, é um prazer ter você conosco.')
    print(Back.LIGHTBLACK_EX + 'PRESSIONE ENTER PARA CONTINUAR...')
    input()
    os.system('cls')
    sprint('Gostaria de ser formal. Qual o seu nome?')
    name = input('>>> ')
    User.append(name)
    editNome()
    sprint(f'É um prazer lhe conhecer, {"".join(User)}.')
    input()
    os.system('cls')
    print(Fore.RED + 'ANFITRIÃO')
    sprint('Pode me chamar de Anfitrião. Serei responsável por guiar você nessa jornada.')
    sprint('Mas antes de tudo, gostaria de dar alguns avisos.')
    input()
    os.system('cls')
    print(Fore.RED + 'ANFITRIÃO')
    sprint('Gostaria de saber qual o seu signo. É importante, para o futuro do seu jogo, claro.')
    sign = input('>>> ')
    Signo.append(sign)
    editSigno()
    if sign.lower() == 'áries' or sign.lower() == 'aries':
        print(Fore.RED +'ANFITRIÃO')
        sprint('Ah, sim. Áries, signo da força.\nEspero que tal força o guie em sua jornada.')
        Signo.append('Áries')
        Planta.append('Ira de Xandoré')
    elif sign.lower() == 'touro':
        print(Fore.RED +'ANFITRIÃO')
        sprint('Ah, sim. Touro, signo da determinação e perseverança.\nEspero que tal resiliência o guie em sua jornada.')
        Signo.append('Touro')
        Planta.append('Hâdia de Rudá')
    elif sign.lower() == 'gêmeos' or sign.lower() == 'gemeos':
        print(Fore.RED +'ANFITRIÃO')
        sprint('Ah, sim. Gêmeos, signo da inteligência.\nEspero que tal curiosidade o guie em sua jornada.')
        Signo.append('Gêmeos')
        Planta.append('Awôto de Polô')
    elif sign.lower() == 'câncer' or sign.lower() == 'cancer':
        print(Fore.RED +'ANFITRIÃO')
        sprint('Ah, sim. Câncer, signo do afeto.\nEspero que tal caridade o guie em sua jornada.')
        Signo.append('Câncer')
        Planta.append('Áuéra de Jaci')
    elif sign.lower() == 'leão' or sign.lower() == 'leao':
        print(Fore.RED +'ANFITRIÃO')
        sprint('Ah, sim. Leão, signo do magnetismo.\nEspero que tal auto-confiança o guie em sua jornada.')
        Signo.append('Leão')
        Planta.append('Alâdia de Guaraci')
    elif sign.lower() == 'virgem':
        print(Fore.RED +'ANFITRIÃO')
        sprint('Ah, sim. Virgem, signo da sabedoria.\nEspero que tal estratégia o guie em sua jornada.')
        Signo.append('Virgem')
        Planta.append('Ewûa de Sumé')
    elif sign.lower() == 'libra':
        print(Fore.RED +'ANFITRIÃO')
        sprint('Ah, sim. Libra, signo da diplomacia.\nEspero que tal empatia o guie em sua jornada.')
        Signo.append('Libra')
        Planta.append('Inkã de Jurupari')
    elif sign.lower() == 'escorpião' or sign.lower() == 'escorpiao':
        print(Fore.RED +'ANFITRIÃO')
        sprint('Ah, sim. Escorpião, signo da intensidade.\nEspero que tal realismo o guie em sua jornada.')
        Signo.append('Escorpião')
        Planta.append('Anhangá')
    elif sign.lower() == 'sagitário' or sign.lower() == 'sagitario':
        print(Fore.RED +'ANFITRIÃO')
        sprint('Ah, sim. Sagitário, signo do otimismo.\nEspero que tal paixão o guie em sua jornada.')
        Signo.append('Sagitário')
        Planta.append('Mangará de Tupã')
    elif sign.lower() == 'capricornio':
        print(Fore.RED +'ANFITRIÃO')
        sprint('Ah, sim. Capricornio, signo da disciplina.\nEspero que tal diligência o guie em sua jornada.')
        Signo.append('Capricornio')
        Planta.append('Fogo de Angra')
    elif sign.lower() == 'aquário' or sign.lower() == 'aquario':
        print(Fore.RED +'ANFITRIÃO')
        sprint('Ah, sim. Aquário, signo da ambição.\nEspero que tal esforço o guie em sua jornada.')
        Signo.append('Aquário')
        Planta.append('Flauta de Akuanbuba')
    elif sign.lower() == 'peixes':
        print(Fore.RED +'ANFITRIÃO')
        sprint('Ah, sim. Peixes, signo da fluidez.\nEspero que tal imaginação o guie em sua jornada.')
        Signo.append('Peixes')
        Planta.append('Rio de Caramuru')
    input('')
    os.system('cls')
    print(Fore.RED + 'ANFITRIÃO')
    sprint('Espero que você tenha consciência do quê está fazendo.')
    answer_menu = input('[1] SIM\n[2] NÃO\n>>> ')
    if answer_menu == '1' or answer_menu.lower() == 's':
        os.system('cls')
        print(Fore.RED + 'ANFITRIÃO')
        sprint('Ah, é ótimo saber disso. Me deixa mais tranquilo saber que cuidará deles.')
        sprint('Creio então que não haja necessidade de explicar o que está fazendo, então podemos prosseguir.')
        answer_menu2 = input('[1] "Não, por favor, me explique!\n[2] "Sim, podemos prosseguir\n>>> ')
        if answer_menu2 == '1':
            os.system('cls')
            print(Fore.RED + 'ANFITRIÃO')
            sprint('Que infortúno. Deveria ter dito que não sabia o que estamos fazendo aqui.\nMas tudo bem.')
            sprint('Estamos brincando com a vida.\nVocê receberá em suas mãos, o controle das decisões de Lara, uma jovem em uma missão.')
            input()
            sprint('Me sinto mal em estragar a suspresa, então espero que se divirta e a conheça melhor.') 
            input()
            sprint('ou não.')
            input()
            sprint('Não sou seu mestre, apenas seu guia.')
            input()
            sprint('Não cabe a mim cuidar de tais intempérios.') 
            input()
            os.system('cls')
            print(Fore.RED + 'ANFITRIÃO')
            print(Fore.RED + 'Essa é sua missão.')
            input()
            os.system('cls')
            print(Fore.RED + 'ANFITRIÃO')
            sprint('No mais, espero que se divirta.')
            input()
            os.system('cls')
            ssprint('Bom jogo...')
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.unload()
            input()
        if answer_menu2 == '2':
            print(Fore.RED + 'ANFITRIÃO')
            sprint('Perfeito!')
            input()
            os.system('cls')
            ssprint('Bom jogo...')
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.unload()
            input()
    elif answer_menu == '2' or answer_menu.lower() == 'n':
        os.system('cls')
        print(Fore.RED + 'ANFITRIÃO')
        sprint('...Não? É uma pena. Não para você, claro. Tenho certeza que irá se divertir tremendamente com a aventura.\n Mas não cabe a você se preocupar com isso.')
        input()
        sprint('Estamos brincando com a vida.\nVocê receberá em suas mãos, o controle das decisões de Lara, uma jovem em uma missão.')
        input()
        sprint('Me sinto mal em estragar a suspresa, então espero que se divirta e a conheça melhor.') 
        input()
        sprint('ou não.')
        input()
        sprint('Não sou seu mestre, apenas seu guia.')
        input()
        sprint('Não cabe a mim cuidar de tais intempérios.') 
        input()
        os.system('cls')
        print(Fore.RED + 'ANFITRIÃO')
        print(Fore.RED + 'Essa é sua missão.')
        input()
        os.system('cls')
        print(Fore.RED + 'ANFITRIÃO')
        sprint('No mais, espero que se divirta.')
        input()
        os.system('cls')
        ssprint('Bom jogo...')
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.unload()
        input()
#Jogo
menu()