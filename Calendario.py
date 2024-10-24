import tkinter as tk
import calendar
import datetime

# Traduzindo os dias e meses para português
dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
meses_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Função para mostrar o calendário
def mostrar_calendario():
    ano = int(ano_entry.get())
    cal_text = [""] * 12
    hoje = datetime.datetime.now()
    dia_atual = hoje.day
    mes_atual = hoje.month

    for mes in range(1, 13):
        cal_mes = calendar.monthcalendar(ano, mes)
        nome_mes = meses_ano[mes - 1]
        cal_texto = f"{nome_mes} {ano}\n"
        cal_texto += " ".join(f"{dia:^3}" for dia in dias_semana) + "\n"
        for semana in cal_mes:
            linha = ""
            for dia in semana:
                if dia != 0 and mes == mes_atual and dia == dia_atual:
                    linha += f"▶{dia:>2} "  # Marcador para o dia atual
                elif dia != 0:
                    linha += f"{dia:>3} "
                else:
                    linha += "    "
            cal_texto += linha + "\n"
        cal_texto += "\n"
        cal_text[mes - 1] = cal_texto

    for i, label in enumerate(cal_labels):
        label.config(text=cal_text[i])

# Função para atualizar a data e hora em tempo real
def atualizar_tempo():
    agora = datetime.datetime.now()
    data_hora.config(text=agora.strftime("%Y-%m-%d %H:%M:%S"))
    janela.after(1000, atualizar_tempo)

# Função para exibir o calendário do ano atual ao iniciar
def exibir_calendario_atual():
    ano_atual = datetime.datetime.now().year
    ano_entry.insert(0, str(ano_atual))
    mostrar_calendario()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calendário Anual")
janela.geometry("800x570")
janela.config(bg='#A9A9A9')

# Configuração do input para o ano
ano_frame = tk.Frame(janela, bg='#A9A9A9')
ano_frame.pack(pady=10)
tk.Label(ano_frame, text="Ano", bg="#A9A9A9").pack(side=tk.LEFT, padx=5)
ano_entry = tk.Entry(ano_frame)
ano_entry.pack(side=tk.LEFT, padx=5)
tk.Button(ano_frame, text="Mostrar Calendário", command=mostrar_calendario, bg="#A9A9A9").pack(side=tk.LEFT, padx=5)

# Frame para exibir o calendário
frame_calendario = tk.Frame(janela, bg='#A9A9A9')
frame_calendario.pack(pady=10)

cal_labels = []
for i in range(12):
    cal_label = tk.Label(frame_calendario, text="", font=('Consolas', 8, 'bold'), bg="#C0C0C0", width=28, height=10, anchor="n")
    cal_label.grid(row=i // 4, column=i % 4, padx=5, pady=5)
    cal_labels.append(cal_label)

cal_label1, cal_label2, cal_label3, cal_label4, cal_label5, cal_label6, cal_label7, cal_label8, cal_label9, cal_label10, cal_label11, cal_label12 = cal_labels

# Label para exibir a data e hora atuais
data_hora = tk.Label(janela, text="", font=('Consolas', 12, 'bold'), bg='#A9A9A9')
data_hora.pack(pady=10)

# Atualizando a hora atual a cada segundo
atualizar_tempo()

# Exibir calendário do ano atual ao iniciar
exibir_calendario_atual()

# Iniciando o loop da interface
janela.mainloop()
