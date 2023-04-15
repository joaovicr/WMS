import Funcoes
import FuncoesRetorna
import Inserir_Dados
from tkinter import ttk
from tkinter.font import Font
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def Funcao_Cadastro(TelaPrincipal):


    TelaPrincipal.update()
    Tela_Cad = tk.Toplevel(TelaPrincipal)
    Tela_Cad.title("CADASTRO DE USUÁRIO")
    Tela_Cad.geometry("1100x700+200+50")
    Tela_Cad.grab_set()

    BordaCima = tk.Frame(Tela_Cad, width=50, height=25, bg="royalblue")
    BordaCima.pack(side="top", fill="both", expand=False)

    fonte_Titulo = Font(size=26, family="Rockwell", weight="bold")
    fonte_Labels = Font(size=20, family="Rockwell", weight="bold")
    fonte_Entrys = Font(size=20, family="Rockwell", weight="bold")

    label_Titulo_Tela = tk.Label(BordaCima, text="CADASTRO DE COLABORADOR", bg="royalblue", font=fonte_Titulo)
    label_Titulo_Tela.pack()


    TelaCorpo = tk.Frame(Tela_Cad, width=500, height=900, bg="gray")
    TelaCorpo.pack(side="top", fill="both", expand=True)


    Tela_Labels = tk.Frame(TelaCorpo, width=200, height=900, bg="gray")
    Tela_Labels.pack(side="left", fill="both", expand=True)

    Tela_entrys = tk.Frame(TelaCorpo, width=200, height=900, bg="gray")
    Tela_entrys.pack(side="left", fill="both", expand=True)

    Tela_Botao = tk.Frame(TelaCorpo, width=100, height=900, bg="gray")
    Tela_Botao.pack(side="left", fill="both", expand=False)





    label_Codigo = tk.Label(Tela_Labels, text="Código:   ", bg="Gray", font=fonte_Labels)
    label_Codigo.pack(side='top', padx=(0, 0), pady=(250, 0),anchor='e')

    label_Nome = tk.Label(Tela_Labels, text="Nome:     ", bg="Gray", font=fonte_Labels)
    label_Nome.pack(side='top', padx=(0, 0), pady=(20, 0), anchor='e')

    label_Senha = tk.Label(Tela_Labels, text="Senha:     ", bg="Gray", font=fonte_Labels)
    label_Senha.pack(side='top', padx=(0, 0), pady=(20, 0), anchor='e')

    label_Situacao = tk.Label(Tela_Labels, text="Situação:", bg="Gray", font=fonte_Labels)
    label_Situacao.pack(side='top', padx=(0, 0), pady=(20, 0), anchor='e')

    Entry_Codigo = tk.Entry(Tela_entrys, width=15, font=fonte_Entrys, borderwidth=2)
    Entry_Codigo.pack(side='top', padx=(0, 0), pady=(254, 0), anchor='w')

    Entry_Nome = tk.Entry(Tela_entrys, width=35, font=fonte_Entrys, borderwidth=2)
    Entry_Nome.pack(side='top', padx=(0, 0), pady=(20, 0), anchor='w')

    Entry_Senha = tk.Entry(Tela_entrys, width=20, font=fonte_Entrys, borderwidth=2, show="*")
    Entry_Senha.pack(side='top', padx=(0, 0), pady=(20, 0), anchor='w')

    Entry_Codigo.focus_set()



    situacao = ["ATIVO", "INATIVO"]

    Combobox_Situacao = ttk.Combobox(Tela_entrys, values=situacao, font=fonte_Entrys,width=19)
    Combobox_Situacao.pack(side='top', padx=(0, 0), pady=(15, 0), anchor='w')



    def Consultar_Codigo(event):
        Codigo = Entry_Codigo.get()
        if not Codigo:
            tela_msgbox = tk.Toplevel(TelaPrincipal)
            tela_msgbox.overrideredirect(True)
            tela_msgbox.geometry('0x0+{}+{}'.format(900, 500))
            tela_msgbox.title("Mensagem")
            messagebox.showinfo("Código em Branco", "Favor Informe um Código!".format(Codigo),
                                parent=tela_msgbox)
            tela_msgbox.destroy()
            Entry_Codigo.focus_set()
        else:
            Entry_Nome.focus_set()
            Codigo = int(Codigo)
            CodigoUsado = Funcoes.PesquisaNomeColaborador(Codigo)
            NomeUsado = Funcoes.PesquisaNomeColaborador(Codigo)
            SenhaUsada = Funcoes.PesquisaSenhaColaborador(Codigo)
            SituacaoUsada = Funcoes.PesquisaSituacaoColaborador(Codigo)
        if not CodigoUsado:
            Entry_Nome.delete(0,999999)
            Entry_Senha.delete(0, 999999)
            Combobox_Situacao.delete(0, 999999)
            Entry_Nome.focus_set()
        else:
            Entry_Nome.insert(0, NomeUsado)
            Entry_Senha.insert(0,SenhaUsada)
            Combobox_Situacao.insert(0,SituacaoUsada)
            Combobox_Situacao.focus_set()
    Entry_Codigo.bind("<Return>", Consultar_Codigo)


    def CadastroNome(event):
        Nome = Entry_Nome.get()
        if not Nome:
            tela_msgbox = tk.Toplevel(TelaPrincipal)
            tela_msgbox.overrideredirect(True)
            tela_msgbox.geometry('0x0+{}+{}'.format(900, 500))
            tela_msgbox.title("Mensagem")
            messagebox.showinfo("Nome em Branco", "Favor Informe um Nome!".format(Nome),
                                parent=tela_msgbox)
            tela_msgbox.destroy()
            Entry_Nome.focus_set()
        else:
            Entry_Senha.focus_set()



    Entry_Nome.bind("<Return>", CadastroNome)

    def CadastroSenha(event):
        Senha = Entry_Senha.get()
        if not Senha:
            tela_msgbox = tk.Toplevel(TelaPrincipal)
            tela_msgbox.overrideredirect(True)
            tela_msgbox.geometry('0x0+{}+{}'.format(900, 500))
            tela_msgbox.title("Mensagem")
            messagebox.showinfo("Senha Vazia", "Favor Informe uma Senha válida!".format(Senha),
                                parent=tela_msgbox)
            tela_msgbox.destroy()
            Entry_Senha.focus_set()
        else:
            Combobox_Situacao.focus_set()

    Entry_Senha.bind("<Return>", CadastroSenha)

    def Funcao_Salvar():
        Codigo = Entry_Codigo.get()
        Nome = Entry_Nome.get()
        Senha = Entry_Senha.get()
        Situacao = Combobox_Situacao.get()
        CodigoUsado = Funcoes.PesquisaNomeColaborador(Codigo)
        if not Situacao or not Senha or not Nome or not Codigo:
            tela_msgbox = tk.Toplevel(TelaPrincipal)
            tela_msgbox.overrideredirect(True)
            tela_msgbox.geometry('0x0+{}+{}'.format(900, 500))
            tela_msgbox.title("Mensagem")
            messagebox.showinfo("Campo em Branco", "Favor preencha todos os campos!".format(Situacao),
                                parent=tela_msgbox)
            tela_msgbox.destroy()
            Combobox_Situacao.focus_set()
        else:
            if not CodigoUsado:
                    Inserir_Dados.Funcao_Inserir_Usuarios(Codigo, Nome, Senha, Situacao)
                    Entry_Codigo.delete(0, 999999)
                    Entry_Nome.delete(0, 999999)
                    Entry_Senha.delete(0, 999999)
                    Combobox_Situacao.delete(0, 999999)
                    Entry_Codigo.focus_set()
            else:
                Inserir_Dados.Funcao_Atualizar_Usuarios(Codigo, Nome, Senha, Situacao)
                Entry_Codigo.delete(0, 999999)
                Entry_Nome.delete(0, 999999)
                Entry_Senha.delete(0, 999999)
                Combobox_Situacao.delete(0, 999999)
                Entry_Codigo.focus_set()





    photosalvar = Image.open("salvar.jpg")
    photosalvar = photosalvar.resize((75, 75), Image.ANTIALIAS)  # ajustar o tamanho da imagem
    photosalvar = ImageTk.PhotoImage(photosalvar)

    botaosalvar = tk.Button(Tela_Botao, image=photosalvar, command=Funcao_Salvar)
    botaosalvar.pack(side='bottom', padx=0, pady=0)


    Tela_Cad.protocol("WM_DELETE_WINDOW", lambda: voltar_tela1(TelaPrincipal, Tela_Cad))

    def voltar_tela1(TelaPrincipal, Tela_Fila):
        # reabilita a tela1
        TelaPrincipal.deiconify()
        TelaPrincipal.state('zoomed')
        Tela_Fila.destroy()

    Tela_Cad.wait_window()