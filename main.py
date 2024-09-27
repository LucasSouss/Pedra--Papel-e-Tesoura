import tkinter
from tkinter import *
from tkinter import ttk

# Importando Pillow
from PIL import Image, ImageTk
import random

#cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha

fundo = "#3b3b3b"

#configurando a janela

janela = Tk()
janela.title('Pedra, Papel e Tesoura - GAME')
janela.geometry('260x280')
janela.configure(bg=fundo)

#dividindo a janela

frame_cima = Frame(janela,width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#configurando o frame cima
# Configurando VOCÊ
app_1 = Label(frame_cima, text='You', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1 , fg=co0)
app_1.place(x=44, y=70)
# Linha lateral
app_1_linha = Label(frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)
# Pontos do Jogador (Você)
app_pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_pontos.place(x=45, y=20)
# dois pontos (:)
app_ = Label(frame_cima, text=':',height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_.place(x=125, y=18)

# Configurando PC
app_2_pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=195, y=20)
app_2 = Label(frame_cima, text='Pc', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=198, y=70)
app_2_linha = Label(frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)

app_linha = Label(frame_cima, text='', width=255, anchor='center', font=('Ivy 1 bold'),bg=co0, fg=co0)
app_linha.place(x=0, y=95)

# Função lógica do jogo

pontos_you = 0
pontos_pc = 0
rondas = 10

# Função para verificar o vencedor
def verificar_vencedor(you, pc):
    # Dicionário que mapeia as combinações em que o jogador ganha
    regras = {
        'stone': 'scissors',  # Pedra ganha de Tesoura
        'scissors': 'paper',  # Tesoura ganha de Papel
        'paper': 'stone'      # Papel ganha de Pedra
    }

    if you == pc:
        return 'Empate'
    
    elif regras[you] == pc:
        return 'Você Ganhou!'
        
    
    else:
        return 'PC Ganhou!'

# Função lógica do jogo
def jogar(i):
    global you, pc
    global rondas
    global pontos_you
    global pontos_pc

    if rondas > 0:
        print(rondas)
        opcoes = ['stone', 'paper', 'scissors']
        pc = random.choice(opcoes)  # Escolha do PC
        you = i  # Escolha do jogador

        # Verifica o vencedor usando a função verificar_vencedor
        resultado = verificar_vencedor(you, pc)

        # Exibe o resultado no console (você pode ajustar para exibir na interface)
        print(f"Você escolheu: {you}, PC escolheu: {pc}. Resultado: {resultado}")

        # Atualiza as rondas e a pontuação conforme o resultado
        if resultado == 'Empate':
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

        elif resultado == 'Você Ganhou!':
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co5
            app_linha['bg'] = co0
            pontos_you += 10

        else: #Pc ganhou!
            app_1_linha['bg'] = co5
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0
            pontos_pc += 10

        # atualização dos pontos
        app_pontos['text'] = pontos_you
        app_2_pontos['text'] = pontos_pc

        rondas -= 1  # Diminui o número de rondas
    else:
        Game_Over()

# FUNÇÃO INICIAR GAME
# configurando frame baixo
    # PEDRA
def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3
    icon_1 = Image.open('images/stone.png')
    icon_1 = icon_1.resize((50,50), Image.LANCZOS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo,command=lambda: jogar('stone'), width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15, y=60)

    # PAPEL
    icon_2 = Image.open('images/paper.png')
    icon_2 = icon_2.resize((50, 50), Image.LANCZOS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo,command=lambda: jogar('paper'), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=95, y=60)

    # TESOURA
    icon_3 = Image.open('images/scissors.png')
    icon_3 = icon_3.resize((50, 50), Image.LANCZOS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo,command=lambda: jogar('scissors'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=170, y=60)

# BOTÃO "PLAY"
b_jogar = Button(frame_baixo, command=iniciar_jogo, width=30, text='PLAY', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=5, y=151)


# Função terminar o jogo
def Game_Over():
    print('Game Over')

janela.mainloop()