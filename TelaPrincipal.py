import Tela_Cad_Usuario
import Tela_Consultar_Enderecos

import tkinter as tk
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
import TelaSeparacaoRetorna
import TelaReposicao

# CRIANDO A JANELA PRINCIPAL DO FRAME
TelaInicial = tk.Tk()
TelaInicial.title("PRINCIPAL")
TelaInicial.state("zoomed")




# CRIANDO OS FRAMES
BordaCima = tk.Frame(TelaInicial,width=50, height=25, bg="royalblue")
BordaCima.pack(side="top", fill="both", expand=True)

TelaBaixo = tk.Frame(TelaInicial,width=500, height=150, bg="gray")
TelaBaixo.pack(side="top", fill="both", expand=True)

TelaLista= tk.Frame(TelaInicial,width=500, height=900, bg="darkgray")
TelaLista.pack(side="top", fill="both", expand=True)


# ALTERAÇÕES DE FONTES

fonte_Titulo = Font(size=26, family="Rockwell", weight="bold")
fonte_Label = Font(size=22, family="Rockwell", weight="bold")
fonte_Entry = Font(size=22, family="Rockwell", weight="bold")

# CRIANDO AS LABELS
label_Titulo_Tela = tk.Label(BordaCima, text="SISTEMA WMS - CONTROLE DE ESTOQUE",bg="royalblue",font=fonte_Titulo)
label_Titulo_Tela.pack()


# CRIANDO AS ENTRY'S



# IMAGENS

photoseparacao = Image.open("separacao1.jpg")
photoseparacao = photoseparacao.resize((180, 100), Image.ANTIALIAS) # ajustar o tamanho da imagem
photoseparacao = ImageTk.PhotoImage(photoseparacao)

photoreposicao = Image.open("reposicao.jpg")
photoreposicao = photoreposicao.resize((180, 100), Image.ANTIALIAS) # ajustar o tamanho da imagem
photoreposicao = ImageTk.PhotoImage(photoreposicao)

photoEnderecamento = Image.open("buscar_endereco.jpg")
photoEnderecamento = photoEnderecamento.resize((180, 100), Image.ANTIALIAS) # ajustar o tamanho da imagem
photoEnderecamento = ImageTk.PhotoImage(photoEnderecamento)

photoUsuario = Image.open("cadUsuario.jpg")
photoUsuario = photoUsuario.resize((180, 100), Image.ANTIALIAS) # ajustar o tamanho da imagem
photoUsuario = ImageTk.PhotoImage(photoUsuario)

# Cria o botão com a imagem
botaoseparacao = Button(TelaBaixo, image=photoseparacao, command=lambda: TelaSeparacaoRetorna.FuncaoListaPedidos(TelaInicial))


botaoreposicao = Button(TelaBaixo, image=photoreposicao, command=lambda: TelaReposicao.FuncaoReposicao(TelaInicial))


botaoEnderecamento = Button(TelaBaixo, image=photoEnderecamento, command=lambda: Tela_Consultar_Enderecos.FuncaoConsultaEnderecos(TelaInicial))

botaoUsuario = Button(TelaBaixo, image=photoUsuario, command=lambda: Tela_Cad_Usuario.Funcao_Cadastro(TelaInicial))



botaoEnderecamento.pack(side='left', anchor=N, padx=(300, 0), pady=(0, 0))
botaoreposicao.pack(side='left', anchor=N, padx=(150, 0), pady=(0, 0))
botaoseparacao.pack(side='left', anchor=N, padx=(150, 0),pady=(0,0))
botaoUsuario.pack(side='left', anchor=N, padx=(150, 0),pady=(0,0))


TelaInicial.mainloop()














#ConexaoTags.ConexaoTAGS()
