import openai
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


# Defina o modelo padrão e os parâmetros
default_model = "text-davinci-003"
default_temperature = 0.7
default_max_tokens = 2032
default_top_p = 1
default_frequency_penalty = 0
default_presence_penalty = 0
default_best_of = 1

# Crie a janela principal
root = tk.Tk()
root.state('zoomed')
root.title("Davinci")
menu_principal = tk.Menu(root)

# Crie as variáveis que armazenarão os valores dos campos
model_var = tk.StringVar(value='text-davinci-003')
model_combobox = ttk.Combobox(root, textvariable=model_var, values=['text-davinci-003', 'text-davinci-002', 'text-davinci-001', 'text-curie-001'])
model_combobox.pack()
temperature_var = tk.DoubleVar(value=default_temperature)
max_tokens_var = tk.IntVar(value=default_max_tokens)
top_p_var = tk.DoubleVar(value=default_top_p)
frequency_penalty_var = tk.DoubleVar(value=default_frequency_penalty)
presence_penalty_var = tk.DoubleVar(value=default_presence_penalty)
best_of_var = tk.IntVar(value=default_best_of)

# Função para exibir a janela "Sobre"
def exibir_sobre():
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Sobre")
    sobre_label = ttk.Label(nova_janela, text="Por Joedson Alves,\nAnalista de compras.")
    sobre_label.pack()
    menu_sobre = tk.Menu(nova_janela)
    menu_sobre.add_command(label="Fechar", command=nova_janela.destroy)
    nova_janela.config(menu=menu_sobre)

# Adicione a opção "Sobre" ao menu principal
menu_principal.add_command(label="Sobre", command=exibir_sobre)


root.config(menu=menu_principal)

# Função para enviar a pergunta ao modelo e mostrar a resposta
def ask_question():
    answer_box.delete("1.0", "end")  # Limpa o campo de resposta
    prompt = input_box.get("1.0", "end-1c")

    openai.api_key = api_key_entry.get()

    model = model_var.get()
    temperature = temperature_var.get()
    max_tokens = max_tokens_var.get()
    top_p = top_p_var.get()
    frequency_penalty = frequency_penalty_var.get()
    presence_penalty = presence_penalty_var.get()
    best_of = best_of_var.get()

    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        best_of=best_of
    )

    answer_box.insert("end", "Davinci:" + response.choices[0].text + "\n")
    input_box.delete("1.0", "end")

# Crie os widgets da interface gráfica
input_label = ttk.Label(root, text="Pergunta:")
input_label.pack()

input_box = ScrolledText(root, height=3, width=200)
input_box.pack()

button = ttk.Button(root, text="Enviar", command=ask_question)
button.pack()

answer_label = ttk.Label(root, text="Resposta:")
answer_label.pack()

answer_box = ScrolledText(root, height=14, width=200)
answer_box.pack()

api_key_label = ttk.Label(root, text="Chave da API:")
api_key_label.pack()

api_key_entry = ttk.Entry(root)
api_key_entry.pack()

temperature_label = ttk.Label(root, text="Temperatura:")
temperature_label.pack()

temperature_scale = ttk.Scale(root, from_=0.0, to=1.0, variable=temperature_var, orient="horizontal", length=200)
temperature_scale.pack()

max_tokens_label = ttk.Label(root, text="Comprimento máximo:")
max_tokens_label.pack()

max_tokens_entry = ttk.Entry(root, textvariable=max_tokens_var)
max_tokens_entry.pack()

top_p_label = ttk.Label(root, text="Top P:")
top_p_label.pack()

top_p_scale = ttk.Scale(root, from_=0.0, to=1.0, variable=top_p_var, orient="horizontal", length=200)
top_p_scale.pack()

frequency_penalty_label = ttk.Label(root, text="Penalidade de frequência:")
frequency_penalty_label.pack()

frequency_penalty_scale = ttk.Scale(root, from_=0.0, to=1.0, variable=frequency_penalty_var, orient="horizontal", length=200)
frequency_penalty_var

frequency_penalty_scale.pack()

presence_penalty_label = ttk.Label(root, text="Penalidade de presença:")
presence_penalty_label.pack()

presence_penalty_scale = ttk.Scale(root, from_=0.0, to=1.0, variable=presence_penalty_var, orient="horizontal", length=200)
presence_penalty_scale.pack()

best_of_label = ttk.Label(root, text="Melhor de:")
best_of_label.pack()

best_of_entry = ttk.Entry(root, textvariable=best_of_var)
best_of_entry.pack()


# Colocar ícone na janela
root.iconbitmap('icon.ico')

# Inicie a janela principal
root.mainloop()
