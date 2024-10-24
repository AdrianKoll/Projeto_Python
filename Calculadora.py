from tkinter import *

# Criando a janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg='white')

# Impedindo redimensionamento
janela.resizable(False, False)

# Definindo cores
cor1 = '#38576b'  # Azul Carregado
cor2 = '#F5FFFA'  # Branco
cor3 = '#FFAB40'  # Laranja
cor4 = '#C0C0C0'  # Cinza

# Definindo fonte
font_1 = ("Ivy", 13, "bold")

# Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Variáveis
todos_valores = ''
valor_texto = StringVar()

# Funções
def entrada_valores(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    try:
        if '%' in todos_valores:
            partes = todos_valores.split('%')
            resultado = eval(partes[0]) * (eval(partes[1]) / 100)
        else:
            resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
    except:
        valor_texto.set("Erro")
        todos_valores = ""

def limpar_valores():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Label de display
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy", 18), bg=cor1)
app_label.place(x=0, y=0)

# Função para criar botões
def criar_botao(comando, texto, largura, altura, x, y, cor):
    Button(frame_corpo, command=comando, text=texto, width=largura, height=altura, font=font_1, relief=RAISED, overrelief=RIDGE, anchor=CENTER, bg=cor).place(x=x, y=y)

# Criando botões
criar_botao(limpar_valores, "C", 13, 2, 0, 0, cor2)
criar_botao(lambda: entrada_valores("%"), "%", 5, 2, 118, 0, cor2)
criar_botao(lambda: entrada_valores("/"), "/", 5, 2, 177, 0, cor3)

criar_botao(lambda: entrada_valores("7"), "7", 5, 2, 0, 52, cor2)
criar_botao(lambda: entrada_valores("8"), "8", 5, 2, 59, 52, cor2)
criar_botao(lambda: entrada_valores("9"), "9", 5, 2, 118, 52, cor2)
criar_botao(lambda: entrada_valores("*"), "*", 5, 2, 177, 52, cor3)

criar_botao(lambda: entrada_valores("4"), "4", 5, 2, 0, 104, cor2)
criar_botao(lambda: entrada_valores("5"), "5", 5, 2, 59, 104, cor2)
criar_botao(lambda: entrada_valores("6"), "6", 5, 2, 118, 104, cor2)
criar_botao(lambda: entrada_valores("+"), "+", 5, 2, 177, 104, cor3)

criar_botao(lambda: entrada_valores("1"), "1", 5, 2, 0, 156, cor2)
criar_botao(lambda: entrada_valores("2"), "2", 5, 2, 59, 156, cor2)
criar_botao(lambda: entrada_valores("3"), "3", 5, 2, 118, 156, cor2)
criar_botao(lambda: entrada_valores("-"), "-", 5, 2, 177, 156, cor3)

criar_botao(lambda: entrada_valores("0"), "0", 13, 2, 0, 208, cor2)
criar_botao(lambda: entrada_valores("."), ".", 5, 2, 118, 208, cor2)
criar_botao(calcular, "=", 5, 2, 177, 208, cor3)

# Iniciando o loop da interface
janela.mainloop()
