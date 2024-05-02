import random
import tkinter as tk
from tkinter import messagebox

def jogar_jogo(escolha_jogador, nome_jogador, window):
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(opcoes)

    resultado = ''

    if escolha_jogador == escolha_computador:
        resultado = 'Empate!'
    elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_jogador == 'papel' and escolha_computador == 'pedra') or \
         (escolha_jogador == 'tesoura' and escolha_computador == 'papel'):
        resultado = f'{nome_jogador} ganhou!'
    else:
        resultado = 'Computador ganhou!'

    messagebox.showinfo("Resultado", f"Você escolheu: {escolha_jogador}\nO computador escolheu: {escolha_computador}\n{resultado}")

def main():
    window = tk.Tk()
    window.title("Jogo de Jokenpo")

    label_instrucao = tk.Label(window, text="Escolha entre pedra, papel ou tesoura e clique em 'Jogar'")
    label_instrucao.grid(row=0, column=0, columnspan=2, pady=10)

    nome_label = tk.Label(window, text="Digite seu nome:")
    nome_label.grid(row=1, column=0, padx=5)

    nome_entry = tk.Entry(window)
    nome_entry.grid(row=1, column=1, padx=5)

    escolha = tk.StringVar(window)
    escolha.set("pedra")

    escolha_label = tk.Label(window, text="Escolha:")
    escolha_label.grid(row=2, column=0, padx=5)

    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_dropdown = tk.OptionMenu(window, escolha, *opcoes)
    escolha_dropdown.grid(row=2, column=1, padx=5)

    def iniciar_jogo():
        nome_jogador = nome_entry.get()
        escolha_jogador = escolha.get()
        if nome_jogador == '':
            messagebox.showwarning("Atenção", "Por favor, digite seu nome.")
        else:
            jogar_jogo(escolha_jogador, nome_jogador, window)

    iniciar_button = tk.Button(window, text="Jogar", command=iniciar_jogo)
    iniciar_button.grid(row=3, columnspan=2, pady=10)

    window.mainloop()

if __name__ == '__main__':
    main()
