import tkinter as tk

def calcular_imc():
    #Função principal para calcular o IMC atráves da altura e peso informados e ao final exibimos para o usuário.
    try:
        valor_peso= peso.get()
        valor_altura= altura.get()
        peso_final=float(valor_peso)
        altura_final=float(valor_altura)
        #Aqui convertemos a altura de cm para m
        altura_final=(altura_final/100)
        #Aqui tratamos o erro de divisão por zero.
        if altura_final<=0 or peso_final<=0:
           mensagem.config(
           text="ERRO, Valores não podem ser menores ou iguais a 0",
           fg= "red",
           bg= "#d6eaf8"
           )
           return 
        imc = peso_final/(altura_final**2)
        #Aqui realizamos a classificação do IMC
        if imc < 18.5:
             mensagem.config(
                  text=f"Seu IMC é{imc:.2f} Está abaixo do peso!!",
                  fg="red" ,
                  bg="#d6eaf8"
             )
        elif   18.5 <= imc <=24.9:
             mensagem.config(
                  text=f"Seu IMC é {imc:.2f} Está no peso normal!!",
                  fg="green" ,
                  bg="#d6eaf8"
             )
        elif   25.0 <= imc <=29.9:
             mensagem.config(
                  text=f"Seu IMC é {imc:.2f} Está em sobrepeso!!",
                  fg="orange" ,
                  bg="#d6eaf8"

             )
        elif  30.0 <= imc <=34.9:
             mensagem.config(
                  text=f"Seu IMC é {imc:.2f} Está em Obesidade(Grau I)!!",
                  fg="red" ,
                  bg="#d6eaf8"
             )
        elif   35.0 <= imc <=39.9:
             mensagem.config(
                  text=f"Seu IMC é {imc:.2f} Está em Obesidade (Grau II)!!",
                  fg="red",
                  bg="#d6eaf8"
             )
        else:
             mensagem.config(
                  text=f"Seu IMC é {imc:.2f} Está em Obesidade mórbida(Grau III)!!",
                  fg="red",
                  bg="#d6eaf8"
             )

#Aqui tratamos o erro dos valores inválidos
    except ValueError:
           mensagem.config(text="ERRO, Digite números válidos!!",fg="red",bg= "#d6eaf8")
           return

def limpar_campos():
    peso.delete(0, tk.END)
    altura.delete(0, tk.END)
    mensagem.config(text="")
    peso.focus()

root = tk.Tk()
root.geometry("600x400")
root.configure(bg = "#d6eaf8")

titulo = tk.Label(root, text = "CALCULADORA DE IMC", bg= "#d6eaf8")
titulo.pack(pady=(10,10))

container = tk.Frame(root, bg= "#d6eaf8")
container.pack(pady =(10,5))

mensagem= tk.Label(container, text= "", fg= "black")
mensagem.grid(row=6, column=0, columnspan=2, pady=15)

LabelPeso= tk.Label(container, text= "Digite seu peso(em KG):", bg = "#d6eaf8")
LabelPeso.grid(row=1, column=0, padx=5, pady= 16)

peso= tk.Entry(container)
peso.grid(row=1, column=1, pady=5)

LabelAltura= tk.Label(container, text= "Digite sua altura (em cm) : ", bg= "#d6eaf8")
LabelAltura.grid(row=2, column=0, padx=5, pady=16)

altura = tk.Entry(container)
altura.grid(row=2, column=1, pady=5)

Calcularbtn = tk.Button(container, text="Calcular IMC", bg= "#3498db" ,activebackground= "#2e86c1" , command=calcular_imc)
Calcularbtn.grid(row=3, column=0, columnspan=2, pady=16)

Limparbtn = tk.Button(container, text="Limpar", bg="#bdc3c7",activebackground= "#aeb6bf", command=limpar_campos)
Limparbtn.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()