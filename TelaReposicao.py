import Buscar_Usuario
import tkinter as tk
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
from tkinter import messagebox
import Inserir_Dados
import Funcoes
import datetime
import Funcoes
import Remover_Dados
import time


def FuncaoReposicao(TelaPrincipal):
    # FUNÇÃO PARA VALIDAÇÕES DOS CAMPOS DA TELA
    def on_enter(event):
        # CAPTURANDO O CODIGO DA TAG
        codigo = Entry_Tag.get()
        # CAPTURANDO O NUMERO DA MATRICULA PARA DEPOIS FORNECER O NOME DA MATRICULA
        CapturarMatricula = Entry_Matricula.get()
        CapturarMatricula = str(CapturarMatricula)
        # CAPTURANDO O ENDEREÇO
        CapturarEndereco = Entry_Endereco.get()
        CapturarEndereco = str(CapturarEndereco)
        # CAPTURA O ITEM (REDUZIDO)
        item_reduzido = Funcoes.Pesquisa_Reduzido(codigo)

        # funcao para verificar se a tag ja tem localizacao
        localizacao = Funcoes.Pesquisa_TAG(codigo)
        if localizacao == codigo:
            tela_msgbox4 = tk.Toplevel(TelaPrincipal)
            tela_msgbox4.overrideredirect(True)
            tela_msgbox4.geometry('0x0+{}+{}'.format(900, 500))
            tela_msgbox4.title("Mensagem")
            pergunta = messagebox.askquestion("ATENÇÃO !","ESSA TAG JA FOI BIPADA EM UM OUTRO ENDEREÇO.\n"
                                                          "Deseja Transferir o item ?",parent = tela_msgbox4)
            if pergunta == 'yes':
                Remover_Dados.Funcao_Remover_tag(localizacao)
                listbox_tags_lidos.insert(END, codigo)
                num_codigos = len(listbox_tags_lidos.get(0, END))
                contador_label.config(text="Quantidade de códigos lidos: " + str(num_codigos))
                engenharia = Funcoes.Pesquisa_Engenharia(item_reduzido)
                Label_Ler_Engenharia.configure(text=engenharia)
                descricao = Funcoes.Descricoes(item_reduzido)
                Label_Ler_Descricao.configure(text=descricao)
                Label_Ler_Reduzido.configure(text=item_reduzido)
                engenhariaPai = Funcoes.Pesquisa_EngenhariaPai(codigo)
                Label_Ler_Engenharia2.configure(text=engenhariaPai)
                Entry_Tag.delete(0, END)
                Entry_Tag.focus_set()
                tela_msgbox4.destroy()
            else:
                if len(listbox_tags_lidos.curselection()) == 1:
                    engenharia = Funcoes.Pesquisa_Engenharia(item_reduzido)
                    descricao = Funcoes.Descricoes(item_reduzido)
                    Label_Ler_Descricao.configure(text=descricao)
                    Label_Ler_Reduzido.configure(text=item_reduzido)
                    Label_Ler_Engenharia.configure(text=engenharia)
                    engenhariaPai = Funcoes.Pesquisa_EngenhariaPai(codigo)
                    Label_Ler_Engenharia2.configure(text=engenhariaPai)
                    Entry_Tag.delete(0, END)
                    Entry_Tag.focus_set()
                    tela_msgbox4.destroy()


                else:
                    Entry_Tag.delete(0, END)
                    Entry_Tag.focus_set()
                    tela_msgbox4.destroy()

        else:

            try:
                engenharia = Funcoes.Pesquisa_Engenharia(item_reduzido)
            except:
                print("nao achou tag na consulta")
            engenhariaPai = Funcoes.Pesquisa_EngenhariaPai(codigo)
            try:
                descricao = Funcoes.Descricoes(item_reduzido)
            except:
                print("nao achou tag na consulta")
            # VALIDAÇÃO PARA SABER SE O CAMPO MATRICULA É VAZIO OU NÃO, CASO SEJA VAZIO ME RETORNE UMA MENSAGEM NA TELA
            if not CapturarMatricula:
                tela_msgbox3 = tk.Toplevel(TelaPrincipal)
                tela_msgbox3.overrideredirect(True)
                tela_msgbox3.geometry('0x0+{}+{}'.format(900, 500))
                tela_msgbox3.title("Mensagem")
                messagebox.showinfo("MATRÍCULA VAZIA",
                                    "Por favor, insira um código de Matrícula válido.".format(CapturarMatricula),
                                    parent=tela_msgbox3)
                tela_msgbox3.destroy()
                Entry_Tag.delete(0, END)
                Entry_Matricula.focus_set()
                return
            # VALIDAÇÃO PARA SABER SE O CAMPO ENDEREÇO É VAZIO OU NÃO, CASO SEJA VAZIO ME RETORNE UMA MENSAGEM NA TELA
            if not CapturarEndereco:
                tela_msgbox4 = tk.Toplevel(TelaPrincipal)
                tela_msgbox4.overrideredirect(True)
                tela_msgbox4.geometry('0x0+{}+{}'.format(900, 500))
                tela_msgbox4.title("Mensagem")
                messagebox.showinfo("ENDEREÇO VAZIO", "Por favor, insira um Endereço válido.".format(CapturarEndereco),
                                    parent=tela_msgbox4)
                tela_msgbox4.destroy()
                Entry_Tag.delete(0, END)
                Entry_Endereco.focus_set()
                return
            # COMANDO PARA SALVAR QUAL FOI O PRIMEIRO CÓDIGO REDUZIDO RECONHECIDO PELO USUÁRIO
            if Label_Ler_Reduzido.cget('text') == '':
                primeiro_item_listbox = item_reduzido
            else:
                primeiro_item_listbox = Label_Ler_Reduzido.cget('text')
            # VALIDAÇÃO PARA SABER SE O USUÁRIO INSERIU ALGUM CÓDIGO REPETIDO,CASO TENHA INSERIDO O CÓDIGO IRÁ PERGUNTAR SE DESEJA MANTER OU RETIRAR
            if codigo in listbox_tags_lidos.get(0, END):
                tela_msgbox = tk.Toplevel(TelaPrincipal)
                tela_msgbox.overrideredirect(True)
                tela_msgbox.geometry('0x0+{}+{}'.format(900, 500))
                tela_msgbox.title("Mensagem")
                teste = messagebox.askquestion("Código já lido", "O código já foi lido \n Deseja Excluir?")
                if teste == "yes":
                    if len(listbox_tags_lidos.curselection()) == 1:
                        index = listbox_tags_lidos.get(0, END).index(codigo)
                        listbox_tags_lidos.delete(index)
                        num_codigos = len(listbox_tags_lidos.get(0, END))
                        contador_label.config(text="Quantidade de códigos lidos: " + str(num_codigos))
                        Label_Ler_Reduzido.configure(text='')
                        Label_Ler_Engenharia.configure(text='')
                        Label_Ler_Descricao.configure(text='')
                        Entry_Tag.delete(0, END)
                        Entry_Tag.focus_set()
                    else:
                        index = listbox_tags_lidos.get(0, END).index(codigo)
                        listbox_tags_lidos.delete(index)
                        num_codigos = len(listbox_tags_lidos.get(0, END))
                        contador_label.config(text="Quantidade de códigos lidos: " + str(num_codigos))

                else:
                    Entry_Tag.delete(0, END)
                    Entry_Tag.focus_set()
                    pass

            else:
                # VALIDAÇÃO PARA SABER SE O TAG QUE FOI INSERIDO POSSUI REDUZIDO, SE NÃO POSSUIR ABRE MENSAGEM DE ERRO... ( CONSIDERAR APENAS SITUAÇÃO = 3 E ESTOQUE = 5 )
                if not item_reduzido:
                    tela_msgbox6 = tk.Toplevel(TelaPrincipal)
                    tela_msgbox6.overrideredirect(True)
                    tela_msgbox6.geometry('0x0+{}+{}'.format(900, 500))
                    tela_msgbox6.title("Mensagem")
                    messagebox.showerror("Valor inválido", "Tag Inválida.", parent=tela_msgbox6)
                    tela_msgbox6.destroy()
                    Entry_Tag.delete(0, END)
                    Entry_Tag.focus_set()
                else:
                    # VALIDAÇÃO PARA SABER SE OS ITENS BIPADOS REFEREM AO MESMO CÓDIGO REDUZIDO INFORMADO NO COMEÇO
                    if item_reduzido == primeiro_item_listbox:
                        listbox_tags_lidos.insert(END, codigo)
                        Label_Ler_Engenharia.configure(text=engenharia)
                        Label_Ler_Reduzido.configure(text=item_reduzido)
                        Label_Ler_Engenharia2.configure(text=engenhariaPai)
                        Label_Ler_Descricao.configure(text=descricao)
                        Entry_Tag.delete(0, END)
                        num_codigos = len(listbox_tags_lidos.get(0, END))
                        contador_label.config(text="Quantidade de códigos lidos: " + str(num_codigos))
                    else:
                        tela_msgbox5 = tk.Toplevel(TelaPrincipal)
                        tela_msgbox5.overrideredirect(True)
                        tela_msgbox5.geometry('0x0+{}+{}'.format(900, 500))
                        tela_msgbox5.title("Mensagem")
                        messagebox.showerror("Valor inválido", "Está tag não corresponde ao SKU do Endereço.",
                                             parent=tela_msgbox5)
                        tela_msgbox5.destroy()
                        Entry_Tag.delete(0, END)
                        Entry_Tag.focus_set()
    # Atualizar a interface do usuário da janela principal antes de abrir a sub-janela

    TelaPrincipal.update()
    Tela_de_Reposicao = tk.Toplevel(TelaPrincipal)
    Tela_de_Reposicao.title("REPOSIÇÃO")
    Tela_de_Reposicao.state("zoomed")
    TelaPrincipal.withdraw()





    # CRIANDO OS FRAMES

    BordaCima = tk.Frame(Tela_de_Reposicao,width=50, height=25, bg="royalblue")
    BordaCima.pack(side="top", fill="both", expand=False)

    TelaCorpo = tk.Frame(Tela_de_Reposicao,width=500, height=900, bg="gray")
    TelaCorpo.pack(side="top", fill="both", expand=True)

    TelaCorpo_ESQUERDO = tk.Frame(TelaCorpo, width=950, height=900, bg="gray")
    TelaCorpo_ESQUERDO.pack(side="left", fill="both", expand=True)

    TelaCorpo_Direito = tk.Frame(TelaCorpo, width=30, height=900, bg="gray")
    TelaCorpo_Direito.pack(side="left", fill="both", expand=False)


    # CRIANDO OS FRAMES DO CORPO
    TelaCorpo_Cima = tk.Frame(TelaCorpo_ESQUERDO, width=90, height=200, bg="gray")
    TelaCorpo_Cima.pack(side="top", fill="both", expand=False)

    TelaCorpo_baixo = tk.Frame(TelaCorpo_ESQUERDO, width=90, height=600, bg="green")
    TelaCorpo_baixo.pack(side="top", fill="both", expand=True)


    # CRIANDO O FRAME DO CORPO DA PARTE DE CIMA
    TelaCorpo_Cima_1_1 = tk.Frame(TelaCorpo_Cima, width=90, height=200, bg="gray")
    TelaCorpo_Cima_1_1.pack(side="left", fill="both", expand=True)

    TelaCorpo_Cima_1_2 = tk.Frame(TelaCorpo_Cima, width=90, height=200, bg="gray")
    TelaCorpo_Cima_1_2.pack(side="left", fill="both", expand=True)

    TelaCorpo_Cima_1_3 = tk.Frame(TelaCorpo_Cima, width=50, height=200, bg="gray")
    TelaCorpo_Cima_1_3.pack(side="left", fill="both", expand=True)

    # CRIANDO O FRAME DO CORPO DA PARTE DE BAIXO

    TelaBaixo1_2_1 = tk.Frame(TelaCorpo_baixo, width=45, height=600, bg="gray")
    TelaBaixo1_2_1.pack(side="left", fill="both", expand=True)

    TelaBaixo1_2_2 = tk.Frame(TelaCorpo_baixo, width=45, height=600, bg="gray")
    TelaBaixo1_2_2.pack(side="left", fill="both", expand=True)


    TelaBaixo1_2_3 = tk.Frame(TelaCorpo_baixo, width=45, height=600, bg="gray")
    TelaBaixo1_2_3.pack(side="left", fill="both", expand=True)




    RodaPe = tk.Frame(Tela_de_Reposicao,width=50, height=25, bg="royalblue")
    RodaPe.pack(side="top", fill="both", expand=False)


    # ALTERAÇÕES DE FONTES

    fonte_Titulo = Font(size=26, family="Rockwell", weight="bold")
    fonte_Label = Font(size=22, family="Rockwell", weight="bold")
    fonte_Entry = Font(size=22, family="Rockwell", weight="bold")
    fonte_Label_Lidas = Font(size=30, family="Rockwell", weight="bold")
    fonte_Label_Nomes = Font(size=10, family="Rockwell", weight="bold")
    fonte_label_contador = Font(size=15, family="Rockwell", weight="bold")


    # CRIANDO AS LABELS
    label_Titulo_Tela = tk.Label(BordaCima, text="REPOSIÇÃO",bg="royalblue",font=fonte_Titulo)
    label_Titulo_Tela.pack()

    Label_Matricula = tk.Label(TelaCorpo_Cima_1_1, text="MATRÍCULA:", width=16, bg="GRAY", foreground="white", font=fonte_Label)

    Label_Ler_Nome = tk.Label(TelaCorpo_Cima_1_3, text="", width=45, bg="GRAY", foreground="black", font=fonte_Label_Nomes)


    Label_Endereco = tk.Label(TelaCorpo_Cima_1_1, text="ENDEREÇO:",width=16,bg="GRAY",foreground="white",font=fonte_Label)


    Label_Ler_Endereco = tk.Label(TelaCorpo_Cima_1_3, text="", width=16, bg="GRAY", foreground="black", font=fonte_Label)


    Label_Tag = tk.Label(TelaCorpo_Cima_1_1, text="TAG:",width=16,bg="GRAY",foreground="white",font=fonte_Label)


    Label_Reduzido = tk.Label(TelaBaixo1_2_1, text="REDUZIDO:",width=16,bg="GRAY",foreground="black",font=fonte_label_contador)


    Label_Ler_Reduzido = tk.Label(TelaBaixo1_2_2,width=8,bg="white",foreground="black",font=fonte_label_contador)


    Label_Engenharia = tk.Label(TelaBaixo1_2_1, text="REFERÊNCIA:",width=16,bg="GRAY",foreground="black",font=fonte_label_contador)


    Label_Ler_Engenharia = tk.Label(TelaBaixo1_2_2,width=14,bg="white",foreground="black",font=fonte_label_contador)


    Label_Descricao = tk.Label(TelaBaixo1_2_1, text="DESCRIÇÃO:",width=16,bg="GRAY",foreground="black",font=fonte_label_contador)


    Label_Ler_Descricao = tk.Label(TelaBaixo1_2_2, width=39, bg="white", foreground="black", font=fonte_label_contador)


    Label_Tag_Lidos = tk.Label(TelaBaixo1_2_3, text="TAG's LIDOS:", width=16, bg="GRAY", foreground="white", font=fonte_Label_Lidas)



    # Labels de Consulta


    Label_Ler_Engenharia2 = tk.Label(TelaCorpo_Cima_1_1, width=15, bg="gray", foreground="gray", font=fonte_label_contador)
    Label_Ler_Engenharia2.place()


    # CRIANDO AS ENTRY'S

    Entry_Matricula = tk.Entry(TelaCorpo_Cima_1_2, width=20, font=fonte_Entry, borderwidth=2)


    # FUNÇÃO PARA SABER QUAL O NOME DO USUÁRIO QUANDO INFORMAR A MATRÍCULA... USA-SE UMA FUNÇÃO
    def atualizar_nome(event):
        CapturarMatricula = Entry_Matricula.get()
        CapturarMatricula = str(CapturarMatricula)
        print(CapturarMatricula)
        nome = Buscar_Usuario.Pesquisa_Nome(CapturarMatricula)
        print(nome)
        if nome:
            Label_Ler_Nome.configure(text=nome)
            Entry_Endereco.focus_set()
            Entry_Matricula.config(state=tk.DISABLED)
        else:
            tela_msgbox2 = tk.Toplevel(TelaPrincipal)
            tela_msgbox2.overrideredirect(True)
            tela_msgbox2.geometry('0x0+{}+{}'.format(900, 500))
            tela_msgbox2.title("Mensagem")
            messagebox.showinfo("MATRÍCULA INVÁLIDA", "Digite uma matrícula existente".format(nome), parent=tela_msgbox2)
            tela_msgbox2.destroy()
            Entry_Matricula.delete(0, END)
            Entry_Matricula.focus_set()

    Entry_Matricula.bind("<Return>", atualizar_nome)

    # FUNÇÃO PARA ESCREVER EM UMA LABEL O ENDEREÇO, PARA DEPOIS LANÇAR ELA NO BANCO DE DADOS
    Entry_Endereco = tk.Entry(TelaCorpo_Cima_1_2, width=20, font=fonte_Entry, borderwidth=2)



    def Ler_Endereco(event):
        CapturarEndereco = Entry_Endereco.get()
        CapturarEndereco = str(CapturarEndereco)
        nome = Funcoes.Pesquisa_Quantidade_NoEndereco(CapturarEndereco)
        Reduzido = Funcoes.Pesquisa_Reduzido_TAG(CapturarEndereco)
        Descricao = Funcoes.Pesquisa_Descricao_Reduzido(Reduzido)
        Engenharia = Funcoes.Pesquisa_Engenharia_Reduzido(Reduzido)
        if not nome:
            nome2 = CapturarEndereco
            Label_Ler_Endereco.configure(text=nome2)
            Entry_Endereco.config(state=tk.DISABLED)
            Entry_Tag.focus_set()
        else:
            tela_msgbox1 = tk.Toplevel(TelaPrincipal)
            tela_msgbox1.overrideredirect(True)
            tela_msgbox1.geometry('0x0+{}+{}'.format(900, 500))
            tela_msgbox1.title("Mensagem")
            resp1 = messagebox.askquestion("ENDEREÇO NÃO ESTÁ VAZIO",
                                           "O Endereço possui {} peça(s)\n\nConfirma Quantidade?".format(nome),
                                           parent=tela_msgbox1)
            if resp1 == 'yes':
                Label_Ler_Reduzido.configure(text=Reduzido)
                Label_Ler_Descricao.configure(text=Descricao)
                Label_Ler_Engenharia.configure(text=Engenharia)
                nome2 = CapturarEndereco
                Label_Ler_Endereco.configure(text=nome2)
                Entry_Endereco.config(state=tk.DISABLED)
                Entry_Tag.focus_set()
                tela_msgbox1.destroy()
            else:
                resp2 = messagebox.askquestion("QUANTIDADE ERRADA",
                                               "Deseja Inventariar o Endereço?\n\nFavor bipar todas as Tag's novamente".format(
                                                   nome), parent=tela_msgbox1)
                if resp2 == 'yes':
                    remover_dados = Remover_Dados.Funcao_Remover(CapturarEndereco)
                    remover_dados
                    nome2 = CapturarEndereco
                    Label_Ler_Endereco.configure(text=nome2)
                    Entry_Endereco.config(state=tk.DISABLED)
                    Entry_Tag.focus_set()
                    tela_msgbox1.destroy()
                else:
                    Label_Ler_Reduzido.configure(text=Reduzido)
                    Label_Ler_Descricao.configure(text=Descricao)
                    Label_Ler_Engenharia.configure(text=Engenharia)
                    nome2 = CapturarEndereco
                    Label_Ler_Endereco.configure(text=nome2)
                    Entry_Endereco.config(state=tk.DISABLED)
                    Entry_Tag.focus_set()
                    tela_msgbox1.destroy()


    Entry_Endereco.bind("<Return>", Ler_Endereco)



    Entry_Tag = tk.Entry(TelaCorpo_Cima_1_2, width=20, font=fonte_Entry, borderwidth=2)
    Entry_Tag.bind("<Return>", on_enter)


 #Label para contar quantos tags foram lidos
    contador_label = Label(TelaBaixo1_2_2, width=30, bg="yellow",  text="Quantidade de códigos lidos: 0",font=fonte_label_contador)


    #LIST BOX QUE SERÃO USADAS
    listbox_tags_lidos = Listbox(TelaBaixo1_2_3, width=25, font=fonte_Entry, borderwidth=2)




    # FUNÇÃO PARA SALVAR NO BANCO DE DADOS, OS CAMPOS NECESSÁRIOS
    def Funcao_Salvar():
        Matricula = Label_Ler_Nome.cget('text')
        Endereco = Label_Ler_Endereco.cget('text')
        Reduzido = Label_Ler_Reduzido.cget('text')
        Data_HoraAtualizacao = datetime.datetime.now()
        Data_HoraAtualizacao_str = Data_HoraAtualizacao.strftime('%d_%m_%Y %H_%M')
        Codigo_Barras2 = listbox_tags_lidos.get(0, END)
        Engenharia = Label_Ler_Engenharia.cget('text')
        EngenhariaPai = Label_Ler_Engenharia2.cget('text')
        Descricao = Label_Ler_Descricao.cget('text')
        try:
            if not Codigo_Barras2:
                raise ValueError("O campo está vazio! Selecionar ao menos um item!")

            for i in range(listbox_tags_lidos.size()):
                Codigo_Barras = listbox_tags_lidos.get(i)
                Inserir_Dados.Funcao_Inserir(Matricula, Codigo_Barras, Reduzido, Endereco, Engenharia, Data_HoraAtualizacao_str, EngenhariaPai, Descricao)
                print(Codigo_Barras)
                print(Reduzido)

            messagebox.showinfo("Sucesso!", "Os dados foram salvos com sucesso")
            Entry_Matricula.config(state='normal')
            Entry_Endereco.config(state='normal')
            Entry_Tag.delete(0, END)
            Entry_Matricula.delete(0, END)
            Entry_Endereco.delete(0, END)
            contador_label.config(text="Quantidade de códigos lidos: 0")
            Label_Ler_Nome.config(text="")
            Label_Ler_Endereco.config(text="")
            Label_Ler_Reduzido.config(text="")
            Label_Ler_Engenharia.config(text="")
            Label_Ler_Engenharia2.config(text="")
            Label_Ler_Descricao.config(text="")
            listbox_tags_lidos.delete(0, END)
            Entry_Matricula.focus_set()

        except ValueError as ve:

            tela_msgbox4 = tk.Toplevel(TelaPrincipal)
            tela_msgbox4.overrideredirect(True)
            tela_msgbox4.geometry('0x0+{}+{}'.format(900,500))
            tela_msgbox4.title("Mensagem")
            messagebox.showerror("Erro!", str(ve), parent=tela_msgbox4)
            tela_msgbox4.destroy()
            Entry_Tag.focus_set()

        except Exception as e:
            messagebox.showinfo("Erro!", "Ocorreu um erro inesperado")

    def execute_crod():
        # Cria uma nova janela de diálogo modal


        dialog = tk.Toplevel()
        dialog.overrideredirect(True)
        dialog.geometry('0x0+{}+{}'.format(900, 500))
        dialog.title("Aguarde...")
        dialog.grab_set()  # Configura a janela como modal


        # Chama a função de CROD
        Funcao_Salvar()

        # Fecha a janela de diálogo e desbloqueia a tela
        dialog.grab_release()
        dialog.destroy()

    def limparDesbloquearLabels():
        Entry_Matricula.config(state='normal')
        Entry_Endereco.config(state='normal')
        Entry_Tag.delete(0, END)
        Entry_Matricula.delete(0, END)
        Entry_Endereco.delete(0, END)
        Label_Ler_Nome.config(text="")
        Label_Ler_Endereco.config(text="")
        Label_Ler_Reduzido.config(text="")
        Label_Ler_Engenharia.config(text="")
        Label_Ler_Engenharia2.config(text="")
        Label_Ler_Descricao.config(text="")
        listbox_tags_lidos.delete(0, END)
        Entry_Matricula.focus_set()





    photosalvar = Image.open("salvar.jpg")
    photosalvar = photosalvar.resize((75, 75), Image.ANTIALIAS)  # ajustar o tamanho da imagem
    photosalvar = ImageTk.PhotoImage(photosalvar)

    # CRIANDO BOTÕES

    botaosalvar = Button(TelaCorpo_Direito, image=photosalvar, command=execute_crod)

# POSICIONANDO OS BLOCOS NA TELA RESPONSIVA

    # 1: posicionar os Label DESCRITIVOS no frame 2_1_1
    Label_Reduzido.pack(side='top',anchor=tk.NE, pady=(100,0))
    Label_Engenharia.pack(side="top", anchor="ne", pady=10)
    Label_Descricao.pack(side="top", anchor="ne")

    # 2: posicionar os Label DE LEITURA no frame 2_1_2
    Label_Ler_Reduzido.pack(side='top',anchor=tk.NW, pady=(100,0))
    Label_Ler_Engenharia.pack(side="top", anchor="nw", pady=10)
    Label_Ler_Descricao.pack(side="top", anchor="nw")
    contador_label.pack(side="top", anchor="nw", pady=50)




    # 1 - listbox

    Label_Tag_Lidos.pack(side='top', anchor=tk.SE, padx=50)
    listbox_tags_lidos.pack(side='top', anchor=tk.SE, padx=50, pady=10)



    Label_Ler_Nome.pack(side='top', anchor=tk.SW, pady=(40,0))
    Label_Ler_Endereco.pack(side='top', anchor=tk.SW,pady=10)


    Label_Matricula.pack(side='top', anchor=tk.SE, pady=(30,0))
    Label_Endereco.pack(side='top', anchor=tk.SE,pady=10)
    Label_Tag.pack(side='top', anchor=tk.SE)

    Entry_Matricula.pack(side='top', anchor=tk.SW, pady=(30,0))
    Entry_Endereco.pack(side='top', anchor=tk.SW,pady=10)
    Entry_Tag.pack(side='top', anchor=tk.SW)

    # 2 botao salvar e Limpar no frame meio
    botaosalvar.pack(side='bottom', anchor=tk.SE, padx=10, pady=10)


    Entry_Tag.focus_set()
    Entry_Matricula.focus_set()



    # CRIANDO BOTÕES

    botao_limpar = Button(TelaCorpo_Direito, text='Limpar', width=16, bg="black", foreground="white", command=limparDesbloquearLabels)
    botao_limpar.pack(side='top',anchor='se')


    Tela_de_Reposicao.protocol("WM_DELETE_WINDOW", lambda: voltar_tela1(TelaPrincipal, Tela_de_Reposicao))

    def voltar_tela1(TelaPrincipal, Tela_de_Reposicao):
        # reabilita a tela1
        TelaPrincipal.deiconify()
        TelaPrincipal.state('zoomed')
        Tela_de_Reposicao.destroy()



    Tela_de_Reposicao.wait_window()

