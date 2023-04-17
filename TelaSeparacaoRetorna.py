import Buscar_Usuario
import FuncoesRetorna
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk, ImageDraw
import math
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

    listas = FuncoesRetorna.TabelaRetorna('1')
    listasColaborador = Buscar_Usuario.PesquisaTodosUsuaios()

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

    TelaDistDivisao = tk.Frame(TelaCorpo, width = 10, height = 800, bg = "royalblue")
    TelaDistDivisao.pack(side="left", fill="both", expand=False)

    TelaDistcorpo = tk.Frame(TelaCorpo, width=200, height=800, bg="white")
    TelaDistcorpo.pack(side="left", fill="both", expand=True)


    # DISTRIBUIR - tela distribuicao

    TelaDistTitulo = tk.Frame(TelaDistcorpo, width=120, height=15, bg="white")
    TelaDistTitulo.pack(side="top", fill="both", expand=False)

    TelaDist = tk.Frame(TelaDistcorpo, width=120, height=775, bg="gray")
    TelaDist.pack(side="top", fill="both", expand=True)

    TelaDistDivisao2 = tk.Frame(TelaDist, width=30, height=775, bg="gray")
    TelaDistDivisao2.pack(side="left", fill="both", expand=False)

    TelaDistDivisao3 = tk.Frame(TelaDist, width=70, height=775, bg="red")
    TelaDistDivisao3.pack(side="left", fill="both", expand=False)
    TelaDistDivisao4 = tk.Frame(TelaDist, width=70, height=775, bg="green")
    TelaDistDivisao4.pack(side="left", fill="both", expand=False)
    TelaDistDivisao5 = tk.Frame(TelaDist, width=70, height=775, bg="red")
    TelaDistDivisao5.pack(side="left", fill="both", expand=False)

    # Obtenha somente os 20 primeiros itens da lista

    fonte_Label = Font(size=16, family="Rockwell",weight="bold")
    fonte_Label2 = Font(size=14, family="Rockwell", weight="bold")
    fonte_Label3 = Font(size=14, family="Rockwell",font='blue')

    labelDistribuicao = tk.Label(TelaDistTitulo,text='DISTRIBUICAO DAS PRE FATURAS', font=fonte_Label, background='white')
    labelDistribuicao.pack(side='top', padx=(0, 0), pady=(0, 0), anchor='center',fill='both')

    QtPaginas = listas["codPedido"].size/20
    QtPaginas = math.ceil(QtPaginas)
    print(QtPaginas)

    frames, notebook = paginar_paginas(QtPaginas, Telatreeview)

    #ACRESCENTANDO OS LABEL NA TELA DE DISTRIBUICAO
    labelNomes = tk.Label(TelaDistDivisao2, text='\nNOME', font=fonte_Label,
                                 background='gray')
    labelNomes.pack(side='top', padx=(0, 0), pady=(0, 0), anchor='nw')
    labelTotalPecas = tk.Label(TelaDistDivisao3, text="TOTAL\n Pç's", font=fonte_Label,
                          background='gray')
    labelTotalPecas.pack(side='top', padx=(0, 0), pady=(0, 0), anchor='nw')
    labelQtdPedidos = tk.Label(TelaDistDivisao4, text="Qtd\n Pedidos", font=fonte_Label,
                               background='gray')
    labelQtdPedidos.pack(side='top', padx=(0, 0), pady=(0, 0), anchor='nw')
    labelMediaPedidos = tk.Label(TelaDistDivisao5, text="Média\nPç's Pedido", font=fonte_Label,
                               background='gray')
    labelMediaPedidos.pack(side='top', padx=(0, 0), pady=(0, 0), anchor='nw')
    try:
        for i in range(listasColaborador.size):
            ColunaNome = listasColaborador['nome'][i]
            label_Nome = tk.Label(TelaDistDivisao2,text=ColunaNome, width=18,font=fonte_Label2,bg='white',anchor='nw' )
            label_Nome.pack(side='top', padx=(0, 0), pady=(0, 0),anchor='nw')
    except:
        print('segue o baile')
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
                    situacao = listasColaborador['nome'].tolist()

                    Combobox_Situacao = ttk.Combobox(Frame_Colabor, values=situacao, font=fonte_Label3, width=19)
                    Combobox_Situacao.pack(side='top', padx=(0, 0), pady=(0, 0), anchor='nw')

                    # Dê o nome da label
                    label.name = label_name
                    checkbox.name = checkbox_name

        except:
            print("segue o baile")




    fonte_Titulo = Font(size=26, family="Rockwell", weight="bold")


    label_Titulo_Tela = tk.Label(BordaCima, text="LISTA DE PEDIDOS", bg="royalblue", font=fonte_Titulo)
    label_Titulo_Tela.pack()




    botaoDetalha = Button(TelaBaixo, image=photoDetalha, background="royalblue")
    botaoDetalha.pack(anchor='w', padx=(10,0))


    Tela_Fila.protocol("WM_DELETE_WINDOW", lambda: voltar_tela1(TelaPrincipal, Tela_Fila))

    def voltar_tela1(TelaPrincipal, Tela_Fila):
        # reabilita a tela1
        TelaPrincipal.deiconify()
        TelaPrincipal.state('zoomed')
        Tela_Fila.destroy()


    Tela_Fila.wait_window()
