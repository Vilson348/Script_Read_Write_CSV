"""
Interface gráfica do Script de leitura e escrita de Arq. CSV
Seleciona os arquivos de entrada, especifica o diretério do arquivo de saída e define o nome do arquivo de saída
"""

from tkinter import *
from tkinter import filedialog
from functools import partial
from datetime import date
import os
#from func_delimiter import func_delimitador
from func_writer import func_chamada_escrita

version = "Versão: 0      "

# Main Window - Creation and Positioning at Center of Screen
root = Tk()
root.title('Modificador de Base de Dados iFix')
width_of_window = 800
height_of_window = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2) - (width_of_window/2)
y_coordinate = (screen_height/2) - (height_of_window/2)
root.geometry('%dx%d+%d+%d' % (width_of_window, height_of_window, x_coordinate, y_coordinate))
root.iconbitmap('tools.ico')

v = IntVar()
v.set(1)
v2 = IntVar()
v2.set(1)
v3 = IntVar()
v3.set(1)
v4 = IntVar()
v4.set(1)
v5 = IntVar()
v5.set(1)
v6 = IntVar()
v6.set(1)
v7 = IntVar()
v7.set(1)
v8 = IntVar()
v8.set(1)
v9 = IntVar()
v9.set(1)
v10 = IntVar()
v10.set(4)
input_param = set()
v11 = IntVar()
v11.set(0)
v12 = IntVar()
v12.set(0)
v13 = IntVar()
v13.set(0)
v14 = IntVar()
v14.set(0)
cbox1_choice = 0
cbox2_choice = 0
cbox3_choice = 0
cbox4_choice = 0

# Background image
photo = PhotoImage(file="bg3.gif")
w = Label(root, image=photo)
w.place(height=400, width=800, x=0, y=0)

# Logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="blue") .grid(row=0, column=0, sticky=W)


def load_bd_btn(args):
    global dataset_name
    global delimiter_charac
    if args == 1:
        ...
        #print("Carregar arquivo de entrada")
    root.input_filename = filedialog.askopenfilename(initialdir="C:/Users/User/Documents/",
                                                     title="Selecione o arquivo de entrada",
                                                     filetypes=(("Arquivos csv", "*.csv"), ("Arquivos txt", "*.txt"),
                                                                ("Todos arquivos", "*.*")))
    dataset_name = os.path.basename(root.input_filename)
    #print(filename)
    input_param.add(2)
# Labels
    my_label = Label(root, text=root.input_filename)
    my_label.place(x=250, y=85)
    split_string = dataset_name.split(".", 1)
    filename2 = split_string[0] + "_" + "Convertida" + "_" + str(date.today()) + '.csv'
    textentry.insert(END, filename2)

# Caracter Delimitador
    delimiter_charac = ";"  # Caracter Delimitador


def load_dir_btn(args):
    global out_dir
    root.input_directory = filedialog.askdirectory(parent=root, initialdir="/", title='Selecione o diretório de saída dos arquivos')
    if args == 3:
        ...
        out_dir = root.input_directory + "/"
        #print(out_dir)
        input_param.add(1)
    # Labels
    my_label = Label(root, text=root.input_directory)
    my_label.place(x=250, y=120)

def process_btn(args):
    global entered_text
    entered_text = textentry.get()  # This will collect the text from the text entry box
    x = len(input_param)
    if args == 4 and len(input_param) >= 3:  # Verifica se todos os 4 Pram. Entrada foram selec.
        # print(entered_text)
        # print(filename)
        arq_saida = out_dir + entered_text
        list1 = [dataset_name, arq_saida, blk_choice, delimiter_charac, cbox1_choice, cbox2_choice, cbox3_choice
            , cbox4_choice]
        func_chamada_escrita(list1)


def blk_rbtn(args):
    global blk_choice
    if args == 1:
        blk_choice = "Games"
    if args == 2:
        blk_choice = "Titanic"
    if args == 3:
        blk_choice = "NBA"
    if blk_choice:
        input_param.add(blk_choice)
    #print(blk_choice)

def cbox1_clicked(args):
    global cbox1_choice
    cbox1_choice = args

def cbox2_clicked(args):
    global cbox2_choice
    cbox2_choice = args

def cbox3_clicked(args):
    global cbox3_choice
    cbox3_choice = args

def cbox4_clicked(args):
    global cbox4_choice
    cbox4_choice = args



# Labels
my_label = Label(root, text="Nome do arquivo de saída: ", relief="raised")
my_label.place(x=10, y=170)
version_label = Label(root, text=version)
version_label.place(x=715, y=0)


# Text entry box
textentry = Entry(root, width=30)
#textentry.insert(END, "BaseDados.csv")
textentry.place(x=252, y=170)

# Create a Frame
# Frame1 Reserva
# frame1 = Frame(root, width=200, height=150, bd=5, bg="white", relief="sunken")
# frame1.place(x=10, y=210)
# Frame2 Blocos
frame2 = Frame(root, width=100, height=90, bd=5, bg="white", relief="sunken")
frame2.place(x=100, y=210)
# Frame3 Blocos
frame3 = Frame(root, width=100, height=90, bd=5, bg="white", relief="sunken")
frame3.place(x=190, y=210)


# Labels of the Frames
blk_label = Label(frame2, text="Grupo", bg="gray", relief="sunken")
blk_label.pack()
blk_label = Label(frame3, text="Parametros", bg="gray", relief="sunken")
blk_label.pack()


# Buttons
btn1 = Button(root, text="Selecione o arquivo de entrada", command=lambda: load_bd_btn(1))  # command - Syntax para passar parâmetro para função
btn1.place(x=10, y=80)
btn3 = Button(root, text="Selecione o caminho do arquivo de saída", command=partial(load_dir_btn, 3))
btn3.place(x=10, y=120)


# Radio Buttons
rbutton_4 = Radiobutton(frame2, text="Games", variable=v10, value=1, command=lambda: blk_rbtn(v10.get()))
rbutton_4.pack(anchor='w')
rbutton_5 = Radiobutton(frame2, text="Titanic", variable=v10, value=2, command=lambda: blk_rbtn(v10.get()))
rbutton_5.pack(anchor='w')
rbutton_6 = Radiobutton(frame2, text="NBA", variable=v10, value=3, command=lambda: blk_rbtn(v10.get()))
rbutton_6.pack(anchor='w')

# Checkboxes
cbox1 = Checkbutton(frame3, text="Grupo", variable=v11, onvalue=1, offvalue=0, command=lambda: cbox1_clicked(v11.get()))
cbox1.pack(anchor='w')
cbox2 = Checkbutton(frame3, text="Coluna1", variable=v12, onvalue=1, offvalue=0, command=lambda: cbox2_clicked(v12.get()))
cbox2.pack(anchor='w')
cbox3 = Checkbutton(frame3, text="Coluna2", variable=v13, onvalue=1, offvalue=0, command=lambda: cbox3_clicked(v13.get()))
cbox3.pack(anchor='w')
cbox4 = Checkbutton(frame3, text="Coluna3", variable=v14, onvalue=1, offvalue=0, command=lambda: cbox4_clicked(v14.get()))
cbox4.pack(anchor='w')

#print(v.get())  # Apenas inprime a variavel v



# Submit Button
submit_button = Button(root, text="PROCESSAR", width=10, command=lambda: process_btn(4), bg="green")
submit_button.place(x=400, y=350)



root.mainloop()

