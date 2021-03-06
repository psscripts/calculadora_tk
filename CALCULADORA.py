from tkinter import *

def click_igual():
	segundo_numero = visor.get()
	visor.delete(0, END)
	if inteiro == 'soma':
		visor.insert(0, p_numero + float(segundo_numero))
	if inteiro == 'subtracao':
		visor.insert(0, p_numero - float(segundo_numero))
	if inteiro == 'multiplicacao':
		visor.insert(0, p_numero * float(segundo_numero))
	if inteiro == 'divisao':
		visor.insert(0, p_numero / float(segundo_numero))


def click_mult():
	primeiro_numero = visor.get()
	global p_numero
	global inteiro
	inteiro = 'multiplicacao'
	p_numero = float(primeiro_numero)
	visor.delete(0, END)

def click_div():
	primeiro_numero = visor.get()
	global p_numero
	global inteiro
	inteiro = 'divisao'
	p_numero = float(primeiro_numero)
	visor.delete(0, END)


def click_sub():
	primeiro_numero = visor.get()
	global p_numero
	global inteiro
	inteiro = 'subtracao'
	p_numero = float(primeiro_numero)
	visor.delete(0, END)


def click_soma():
	primeiro_numero = visor.get()
	global p_numero
	global inteiro
	inteiro = 'soma'
	p_numero = float(primeiro_numero)
	visor.delete(0, END)


def delete():
	visor.delete(0, END)

def click_ponto():
	visor.insert(END, '.')

def click_button(numero):
	atual = visor.get()
	visor.delete(0, END)
	visor.insert(END, str(atual)+ str(numero))

	
		
	
janela = Tk()


janela.title("CALCULADORA")#titulo
janela.resizable(False, False)
#janela.configure(background="")

texto = Label(janela, text="CALCULADORA", font=("arial", 10, 'bold'), pady=10)
texto.pack()


visor = Entry(janela, bg="lightblue")
visor.pack()
visor.place(x=180, y=100)

#linha 1
bt1 = Button(janela, text="1", bg="lightblue", pady=14, padx=14, bd=25, command=lambda: 	click_button(1))

bt1.place(x=30, y=200)


bt2 = Button(janela, text="2", bg="lightblue", pady=14, padx=14, bd=25, command=lambda: click_button(2))

bt2.place(x=30, y=327)

bt3 = Button(janela, text="3", bg="lightblue", pady=14, padx=14, bd=25, command=lambda: click_button(3))
bt3.place(x=30, y=455)

bt0 = Button(janela, text="0", bg="lightblue", pady=14, padx=14, bd=25, command=lambda: click_button(0))
bt0.place(x=30, y=590)

#linha 2
bt4 = Button(janela, text="4", bg="lightblue", pady=14, padx=14, bd=25, command=lambda: click_button(4))
bt4.place(x=160, y=200)

bt5 = Button(janela, text="5", bg="lightblue", pady=14, padx=14, bd=25, command=lambda: click_button(5))
bt5.place(x=160, y=330)

bt6 = Button(janela, text="6", bg="lightblue", pady=14, padx=14, bd=25, command=lambda: click_button(6))
bt6.place(x=160, y=455)

#linha 3

bt7 = Button(janela, text="7", bg="lightblue", pady=14, padx=14, bd=25,command=lambda: click_button(7))
bt7.place(x=290, y=200)

bt8 = Button(janela, text="8", bg="lightblue", pady=14, padx=14, bd=25, command=lambda: click_button(8))
bt8.place(x=290, y=329)

bt9 = Button(janela, text="9", bg="lightblue", pady=14, padx=14, bd=25, command=lambda: click_button(9))
bt9.place(x=290, y=455)

#ponto
btponto = Button(janela, text=".", bg="lightblue", pady=14, padx=14, bd=25, command=click_ponto)
btponto.place(x=290, y=590)

#limpar
btlimpar = Button(janela, text="LIMPAR", pady=119, padx=14, bd=14, command=delete)
btlimpar.place(x=530, y=210)

#somar
btsoma = Button(janela, text="+", bg='lightblue', pady=14, padx=14, bd=25, command=click_soma)
btsoma.place(x=400, y=200)


btsubtracao = Button(janela, text="-", bg='lightblue', pady=14, padx=14, bd=25, command=click_sub)
btsubtracao.place(x=401, y=330)

btdivisao = Button(janela, text="/", bg='lightblue', pady=14, padx=14, bd=25, command=click_div)
btdivisao.place(x=400, y=455)

btmult = Button(janela, text="??", bg='lightblue', pady=14, padx=14, bd=25, command=click_mult)
btmult.place(x=400, y=590)


btigual = Button(janela, text="=", bg='lightblue', pady=14, padx=14, bd=25, command=click_igual)
btigual.place(x=158, y=590)


janela.mainloop()