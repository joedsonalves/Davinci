# Davinci
A simple Python graphical user interface that allows you to interact with the OpenAI API. Through this application, you can send questions or statements and get an AI-generated response. The response parameters can be adjusted to obtain more precise results.

# OpenAI API Interface

This Python script provides a simple graphical interface to interact with the OpenAI API. It allows you to ask a question or make a statement, and the AI will provide a response based on the parameters set.

## Prerequisites

- Python 3
- `openai` module
- `tkinter` module
- `scrolledtext` module

To install the required modules, run the following command in your terminal:

pip install openai tkinter




## Usage

1. Replace `"Your API KEY here"` with your actual API key obtained from OpenAI.
2. Run the script in your terminal by running `python openai_interface.py`.
3. Enter your question or statement in the input field.
4. Adjust the parameters to fine-tune the response.
5. Click the "Enviar" button to send your question/statement to the AI and receive a response.

## Parameters

- **Model**: Select the language model to use. The available models are `text-davinci-003`, `text-davinci-002`, `text-davinci-001`, and `text-curie-001`. Keep in mind that while `text-davinci-003` is the most expensive option, it is also the most effective model available.
- **Temperatura**: Controls the degree of randomness in the response. A higher temperature value will result in more unpredictable and creative responses, while a lower value will result in more conservative and safe responses.
- **Comprimento máximo**: Sets the maximum length of the response in tokens. A token is a word or punctuation mark.
- **Top P**: Controls the diversity of the response. A higher top P value will result in more diverse and varied responses, while a lower value will result in more similar and repetitive responses.
- **Penalidade de frequência**: Penalizes the model for repeating the same words or phrases multiple times in the response. A higher penalty value will result in fewer repeated words or phrases.
- **Penalidade de presença**: Penalizes the model for using words or phrases that are not relevant to the context of the question/statement. A higher penalty value will result in more relevant responses.
- **Melhor de**: Controls the number of responses generated by the model. The highest scoring response will be returned as the final result.

## Example with API KEY directly in the code.

```python
import openai
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

# Replace "Your API KEY here" with your actual API key obtained from OpenAI.
openai.api_key = "Your API KEY here"

# Define the default model and parameters
default_model = "text-davinci-003"
default_temperature = 0.7
default_max_tokens = 2032
default_top_p = 1
default_frequency_penalty = 0
default_presence_penalty = 0
default_best_of = 1

# Create the main window
root = tk.Tk()
root.state('zoomed')
root.title("Davinci")
menu_principal = tk.Menu(root)

## Create the variables to store the field values

# Model: Select the language model to use. The available models are text-davinci-003, text-davinci-002, text-davinci-001, and text-curie-001.

model_var = tk.StringVar(value=default_model)
model_combobox = ttk.Combobox(root, textvariable=model_var, values=['text-davinci-003', 'text-davinci-002', 'text-davinci-001', 'text-curie-001'])
model_combobox.pack()

# Temperature: Controls the degree of randomness in the response. A higher temperature value will result in more unpredictable and creative responses, while a lower value will result in more conservative and safe responses.

temperature_var = tk.DoubleVar(value=default_temperature)

# Max Tokens: Sets the maximum length of the response in tokens. A token is a word or punctuation mark.

max_tokens_var = tk.IntVar(value=default_max_tokens)

# Top P: Controls the diversity of the response. A higher top P value will result in more diverse and varied responses, while a lower value will result in more similar and repetitive responses.

top_p_var = tk.DoubleVar(value=default_top_p)

# Frequency Penalty: Penalizes the model for repeating the same words or phrases multiple times in the response. A higher penalty value will result in fewer repeated words or phrases.

frequency_penalty_var = tk.DoubleVar(value=default_frequency_penalty)

# **Presence Penalty:** Penalizes the model for using words or phrases that are not relevant to the context of the question/statement. A higher penalty value will result in more relevant responses.

presence_penalty_var = tk.DoubleVar(value=default_presence_penalty)

# **Best Of:** Controls the number of responses generated by the model. The highest scoring response will be returned as the final result.

best_of_var = tk.IntVar(value=default_best_of)

# Function to display the "About" window
def exibir_sobre():
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Sobre")
    sobre_label = ttk.Label(nova_janela, text="Por Joedson Alves,\nAnalista de compras.")
    sobre_label.pack()
    menu_sobre = tk.Menu(nova_janela)
    menu_sobre.add_command(label="Fechar", command=nova_janela.destroy)
    nova_janela.config(menu=menu_sobre)

# Add the "About" option to the main menu.
menu_principal.add_command(label="Sobre", command=exibir_sobre)


root.config(menu=menu_principal)

# Function to send the question to the model and display the answer.
def ask_question():
    answer_box.delete("1.0", "end")  # Limpa o campo de resposta
    prompt = input_box.get("1.0", "end-1c")

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

    answer_box.insert("end", "Davinci: " + response.choices[0].text + "\n")
    input_box.delete("1.0", "end")

# Create the widgets for the graphical user interface.
input_label = ttk.Label(root, text="Pergunta:")
input_label.pack()

input_box = ScrolledText(root, height=4, width=200)
input_box.pack()

button = ttk.Button(root, text="Enviar", command=ask_question)
button.pack()

answer_label = ttk.Label(root, text="Resposta:")
answer_label.pack()

answer_box = ScrolledText(root, height=16, width=200)
answer_box.pack()

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


root.iconbitmap('icon.ico')


# Start the main window.
root.mainloop()
```

## Image of the compiled script from the repository.
![Davinci.py](https://github.com/joedsonalves/Davinci/blob/main/API.png)

## Recommendations
To use the OpenAI tool, you have the option of downloading the repository or using example code. If you choose to download the repository, you will need to download the .rar files named `"Davinci.part1.rar"`, `"Davinci.part2.rar"`, and `"Davinci.part3.rar"`. Only one of these .rar files needs to be unpacked and installed, but all three .rar files must be in the same folder for the installation to work. There is no need to unpack all three files.

The above script was developed to make using the OpenAI tool more convenient. By integrating the API directly into the script, the program can be executed without any additional setup. Conversely, the executable version requires the user to manually input the API into the graphical interface. Therefore, if you have Python installed and plan to use the tool frequently, it is recommended that you compile the example code with the OpenAI API. For casual users, it is more convenient to simply download the repository and input the API into the graphical interface as instructed.


## Conclusion
In this script, we created a simple graphical interface to interact with the OpenAI API. The interface allows users to ask questions or make statements and receive responses based on parameters set in the interface. We also covered the various parameters that can be adjusted to fine-tune the response from the AI, including the model, temperature, maximum length, top P, frequency penalty, presence penalty, and best of. With this interface, users can experiment with the various parameters and see how they affect the AI's response.


## License
This project is licensed under the MIT License - see the LICENSE file for details.
