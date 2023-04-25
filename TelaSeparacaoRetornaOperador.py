import Buscar_Usuario
import FuncoesRetorna
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk, ImageDraw
import math

import Inserir_Dados


#teste git

def paginar_paginas(num_paginas, frame):
    notebook = ttk.Notebook(frame, style='TNotebook')

    frames = []
    for i in range(num_paginas):
        frame = tk.Frame(notebook, background='gray')
        frames.append(frame)
        notebook.add(frame, text=f" {i+1}")

    notebook.pack(expand=True, fill="both", side="bottom")

    return frames, notebook


def FuncaoListaPedidos(TelaPrincipal):



    photoDetalha = Image.open("DetalhaPedido.jpg")
    photoDetalha = photoDetalha.resize((100, 30), Image.ANTIALIAS)  # ajustar o tamanho da imagem
    photoDetalha = ImageTk.PhotoImage(photoDetalha)

    photoAtualizar = Image.open("Atualizar.png")
    photoAtualizar = photoAtualizar.resize((100, 30), Image.ANTIALIAS)  # ajustar o tamanho da imagem
    photoAtualizar = ImageTk.PhotoImage(photoAtualizar)

    listas = FuncoesRetorna.TabelaRetorna('1')
    Distribuicao = FuncoesRetorna.Distribuicao('1')
    listasColaborador2 = Buscar_Usuario.PesquisaTodosUsuaios()

    TelaPrincipal.update()
    Tela_Fila = tk.Toplevel(TelaPrincipal)
    Tela_Fila.title("CONSULTA ENDEREÇOS")
    Tela_Fila.state("zoomed")
    Tela_Fila.grab_set()

    BordaCima = tk.Frame(Tela_Fila, width=50, height=25, bg="royalblue")
    BordaCima.pack(side="top", fill="both", expand=False)

    TelaBaixo = tk.Frame(Tela_Fila, width=500, height=50, bg="royalblue")
    TelaBaixo.pack(side="bottom", fill="both", expand=False)

    TelaCorpo = tk.Frame(Tela_Fila, width=500, height=900, bg="gray")
    TelaCorpo.pack(side="top", fill="both", expand=True)

    Telatreeview = tk.Frame(TelaCorpo, width=400, height=800, bg="gray")
    Telatreeview.pack(side="left", fill="both", expand=True)


    # Obtenha somente os 20 primeiros itens da lista

    fonte_Label = Font(size=16, family="Rockwell",weight="bold")
    fonte_Label2 = Font(size=14, family="Rockwell", weight="bold")
    fonte_Label3 = Font(size=14, family="Rockwell",font='blue')
    fonte_Label4 = Font(size=11, family="Rockwell", font='blue')



    totalRetrona = listas["sugerido"].sum()
    totalRetronaPACO = listas[listas["MARCA"] == 'PACO']
    totalRetronaPACO =totalRetronaPACO["sugerido"].sum()
    totalRetronaMpollo = listas[listas["MARCA"] == 'M.POLLO']
    totalRetronaMpollo =totalRetronaMpollo["sugerido"].sum()




    QtPaginas = listas["codPedido"].size/20
    QtPaginas = math.ceil(QtPaginas)
    print(QtPaginas)

    frames, notebook = paginar_paginas(QtPaginas, Telatreeview)



    labelsTotal = []



    #ACRESCENTANDO OS LABEL NA TELA DE PEDIDOS A SEPARTAR
    for i in range(QtPaginas):
        Frame_checkbox = tk.Frame(frames[i], width=20, height=800, bg="gray")
        Frame_checkbox.pack(side='left', padx=(25, 0), pady=(0, 0), anchor='nw')
        Frame_Pedidos = tk.Frame(frames[i], width=20, height=800, bg="gray")
        Frame_Pedidos.pack(side='left', padx=(0, 0), pady=(0, 0), anchor='nw')
        Frame_Sugerido = tk.Frame(frames[i], width=20, height=800, bg="gray")
        Frame_Sugerido.pack(side='left', padx=(0, 0), pady=(0, 0), anchor='nw')
        Frame_Cliente = tk.Frame(frames[i], width=20, height=800, bg="gray")
        Frame_Cliente.pack(side='left', padx=(0, 0), pady=(0, 0), anchor='nw')
        Frame_MARCA = tk.Frame(frames[i], width=20, height=800, bg="gray")
        Frame_MARCA.pack(side='left', padx=(0, 0), pady=(0, 0), anchor='nw')
        Frame_Data = tk.Frame(frames[i], width=20, height=800, bg="gray")
        Frame_Data.pack(side='left', padx=(0, 0), pady=(0, 0), anchor='nw')
        Frame_Colabor = tk.Frame(frames[i], width=20, height=800, bg="gray")
        Frame_Colabor.pack(side='left', padx=(0, 0), pady=(0, 0), anchor='nw')


        label_Titulo_Pedidos = ttk.Label(Frame_Pedidos, text="\nVALOR", width=10, font=fonte_Label2, anchor='center', background='gray')
        label_Titulo_Pedidos.pack(side='top', padx=(0, 0), pady=(0, 0), anchor='nw')
        label_Titulo_SELECAO = ttk.Label(Frame_checkbox, text="\nPEDIDOS", width=11, font=fonte_Label2, background='gray')
        label_Titulo_SELECAO.pack(side='top', padx=(0, 0), pady=(0, 0), anchor='center')
        label_Titulo_Sugerido = ttk.Label(Frame_Sugerido, text="QNT.\nPEÇAS", width=11, font=fonte_Label2, background='gray', anchor='center')
        label_Titulo_Sugerido.pack(side='top', padx=(0, 0), pady=(0, 0), anchor='center')
        label_Titulo_cliente = ttk.Label(Frame_Cliente, text="COD.\nCLIENTE", width=11, font=fonte_Label2, background='gray',anchor='center')
        label_Titulo_cliente.pack(side='top', padx=(0, 0), pady=(0, 0),anchor='center')
        label_Titulo_MARCA = ttk.Label(Frame_MARCA, text="\nMARCA", width=11, font=fonte_Label2, background='gray',anchor='center')
        label_Titulo_MARCA.pack(side='top', padx=(0, 0), pady=(0, 0),anchor='center')
        label_Titulo_Data = ttk.Label(Frame_Data, text="Data\n Geracao", width=11, font=fonte_Label2, background='gray',anchor='center')
        label_Titulo_Data.pack(side='top', padx=(0, 0), pady=(0, 0),anchor='center')
        label_Titulo_Pedidos = ttk.Label(Frame_Colabor, text="Atribuir\nPara", width=13, font=fonte_Label2, anchor='center', background='gray')
        label_Titulo_Pedidos.pack(side='top', padx=(0, 0), pady=(0, 0), anchor='nw')

         # Crie um estilo personalizado para a Checkbutton
        style = ttk.Style()
        style.configure('Custom.TCheckbutton', font=('Rockwell', 16))
        ValorInicial = i*20
        valorFinal = (i+1)*20
        lista_Pag1 = listas[ValorInicial:valorFinal]


        # Percorra a lista e crie uma label para cada índice
        try:
            for item in range(22):

                # Obtenha o item da coluna 1 da sublista
                coluna1 = listas["codPedido"][item+i*22]
                coluna2 = listas["vlrSugestao"][item+i*22]
                coluna3 = listas["codCliente"][item+i*22]
                coluna4 = listas["sugerido"][item+i*22]
                coluna5 = listas["MARCA"][item+i*22]
                coluna6 = listas["DataGeracao"][item+i*22]
                # Crie o nome da label
                label_name = "{}".format(coluna1)
                # Crie a label com o item da coluna 1
                label = ttk.Label(Frame_Pedidos, text='R$  ' + str(coluna2),width=10,font=fonte_Label,anchor='center')
                label2 = ttk.Label(Frame_Sugerido, text=coluna4,width=10,font=fonte_Label,anchor='center')
                label3 = ttk.Label(Frame_Cliente, text=str(coluna3), width=10, font=fonte_Label,anchor='center')
                label4 = ttk.Label(Frame_MARCA, text=str(coluna5), width=10, font=fonte_Label,anchor='center')
                label5 = ttk.Label(Frame_Data, text=str(coluna6), width=10, font=fonte_Label, anchor='center')

                # Crie o nome do checkbox
                checkbox_name = "checkbox_{}".format(item)
                # Crie o checkbox vinculado à respectiva label
                checkbox = ttk.Checkbutton(Frame_checkbox, text=label_name, command=lambda: print(checkbox_name),style='Custom.TCheckbutton', width=10)
                checkbox.var = tk.BooleanVar()
                checkbox.configure(variable=checkbox.var, onvalue=True, offvalue=False)
                checkbox.configure(command=lambda: print("Checkbox {} status: {}".format(checkbox_name, checkbox.var.get())))
                checkbox.pack(side='top',padx=(0,0), pady=(0,0), anchor='e')
                # Adicione a label ao root
                label.pack(side='top',padx=(0,0), anchor='nw')
                label2.pack(side='top', padx=(0, 0), anchor='e', fill='both')
                label3.pack(side='top', padx=(0, 0), anchor='e', fill='both')
                label4.pack(side='top', padx=(0, 0), anchor='e', fill='both')
                label5.pack(side='top', padx=(0, 0), anchor='e', fill='both')
                situacao = listasColaborador2['nome'].tolist()

                # Dê o nome da label
                label.name = label_name
                checkbox.name = checkbox_name

        except:
            print("segue o baile")




    fonte_Titulo = Font(size=26, family="Rockwell", weight="bold")


    label_Titulo_Tela = tk.Label(BordaCima, text="LISTA DE PEDIDOS: NOME", bg="royalblue", font=fonte_Titulo)
    label_Titulo_Tela.pack()



    def atualizar():
        print('teste')
        AtualizanrDistribuicao = FuncoesRetorna.Distribuicao('1')
        AtualizanrDistribuicao2 = Buscar_Usuario.PesquisaTodosUsuaios()
        for i in range(AtualizanrDistribuicao2.size):
            ColunaTotal = AtualizanrDistribuicao['total_peças'][i]
            labelsTotal[i].config(text=ColunaTotal)


    botaoDetalha = Button(TelaBaixo, image=photoDetalha, background="royalblue", command= atualizar)
    botaoDetalha.pack(anchor='w', padx=(10, 0))

        # aqui você pode adicionar os widgets que deseja ao TelaDist



    #botaoAtualizar = Button(BordaCima, image=photoAtualizar, background="royalblue", command= atualizar)
    #botaoAtualizar.pack(anchor='e', padx=(0,0))


    Tela_Fila.protocol("WM_DELETE_WINDOW", lambda: voltar_tela1(TelaPrincipal, Tela_Fila))

    def voltar_tela1(TelaPrincipal, Tela_Fila):
        # reabilita a tela1
        TelaPrincipal.deiconify()
        TelaPrincipal.state('zoomed')
        Tela_Fila.destroy()


    Tela_Fila.wait_window()
