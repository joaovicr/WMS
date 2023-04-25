import Funcoes
import Tela_Cad_Usuario
import Tela_Consultar_Enderecos
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
import TelaSeparacaoRetorna
import TelaReposicao
from tkinter import messagebox

usuario = ""


def Tela_Principal():
    # CRIANDO A JANELA PRINCIPAL DO FRAME
    TelaInicial = tk.Tk()
    TelaInicial.title("PRINCIPAL")
    TelaInicial.state("zoomed")



    fonte_Titulo = Font(size=26, family="Rockwell", weight="bold")
    fonte_Label = Font(size=22, family="Rockwell", weight="bold")
    fonte_Label_Erro = Font(size=16, family="Rockwell", weight="bold")
    fonteLabelMenor = Font(size=12, family="Rockwell", weight="bold")
    # CRIANDO OS FRAMES
    BordaCima = tk.Frame(TelaInicial,width=50, height=25, bg="royalblue")
    BordaCima.pack(side="top", fill="both", expand=False)


    # CRIANDO AS LABELS
    label_Titulo_Tela = tk.Label(BordaCima, text="WMS",bg="royalblue",font=fonte_Titulo)
    label_Titulo_Tela.pack(side='left', anchor='e', padx=(780,0))

    TelaBaixo = tk.Frame(TelaInicial,width=500, height=100, bg="darkgray")
    TelaBaixo.pack(side="top", fill="both", expand=False)

    TelaLista= tk.Frame(TelaInicial,width=500, height=900, bg="darkgray")
    TelaLista.pack(side="top", fill="both", expand=True)

    TelaLista1= tk.Frame(TelaLista,width=500, height=500, bg="darkgray")
    TelaLista1.pack(side="top", fill="both", expand=False)

    TelaLista1_0 = tk.Frame(TelaLista1, width=250, height=300, bg="darkgray")
    TelaLista1_0.pack(side="top", fill="both", expand=False)


    TelaLista1_1= tk.Frame(TelaLista1,width=250, height=200, bg="darkgray")
    TelaLista1_1.pack(side="left", fill="both", expand=True)

    TelaLista1_2= tk.Frame(TelaLista1,width=250, height=200, bg="darkgray")
    TelaLista1_2.pack(side="left", fill="both", expand=True)

    TelaLista2= tk.Frame(TelaLista,width=500, height=150, bg="darkgray")
    TelaLista2.pack(side="top", fill="both", expand=False)

    # ALTERAÇÕES DE FONTES


    labelERRO = tk.Label(TelaLista1_0, bg="darkgray", font=fonte_Label, fg="darkgray")
    labelERRO.pack(side='bottom', anchor='center', padx=(10, 0), pady=(10, 0))
    def mudarCor():
        labelERRO.configure(bg="firebrick", fg="white", text="Preencha todos os campos!", bd=2, relief="groove", font=fonte_Label_Erro)  # Mudando a cor da Label para vermelho após 1 segundo
        labelERRO.after(5000, lambda: labelERRO.configure(bg="darkgray", fg="darkgray", bd=0, relief="flat"))  # Voltando a cor original após 5 segundos

    def UsuarioNaoEncontrado():
        labelERRO.configure(bg="firebrick", fg="white", text="Usuário não Encontrado!", bd=2, relief="groove", font=fonte_Label_Erro)  # Mudando a cor da Label para vermelho após 1 segundo
        labelERRO.after(5000, lambda: labelERRO.configure(bg="darkgray", fg="darkgray", bd=0, relief="flat"))  # Voltando a cor original após 5 segundos

    def SenhaNaoEncontrado():
        labelERRO.configure(bg="firebrick", fg="white", text="Senha Inválida!", bd=2, relief="groove", font=fonte_Label_Erro)  # Mudando a cor da Label para vermelho após 1 segundo
        labelERRO.after(5000, lambda: labelERRO.configure(bg="darkgray", fg="darkgray", bd=0, relief="flat"))  # Voltando a cor original após 5 segundos

    def UsuarioComLetra():
        labelERRO.configure(bg="firebrick", fg="white", text="Digite sua Matrícula, Apenas Números!", bd=2,relief="groove", font=fonte_Label_Erro)  # Mudando a cor da Label para vermelho após 1 segundo
        labelERRO.after(5000, lambda: labelERRO.configure(bg="darkgray", fg="darkgray", bd=0,relief="flat"))  # Voltando a cor original após 5 segundos

    labelNomeLogin = tk.Label(TelaLista1_1, text="Usuário:",bg="royalblue",font=fonte_Label, width=10)
    labelNomeLogin.pack(side='top', padx=(0, 0), pady=(10, 0), anchor='e')

    labelSenhaLogin = tk.Label(TelaLista1_1, text="Senha:",bg="royalblue",font=fonte_Label, width=10)
    labelSenhaLogin.pack(side='top', padx=(0, 0), pady=(20, 0), anchor='e')

    Entry_Nome = tk.Entry(TelaLista1_2, width=20, font=fonte_Label, borderwidth=2)
    Entry_Nome.pack(side='top', padx=(0, 0), pady=(10, 0), anchor='w')
    Entry_Nome.focus_set()
    Entry_Nome.configure(justify='center')

    Entry_Senha = tk.Entry(TelaLista1_2, width=20, font=fonte_Label, borderwidth=2, show="*")
    Entry_Senha.pack(side='top', padx=(0, 0), pady=(20, 0), anchor='w')
    Entry_Senha.configure(justify='center')


    # CRIANDO AS ENTRY'S



    # IMAGENS

    photoDistribuicao = Image.open("Distribuicao.jpg")
    photoDistribuicao = photoDistribuicao.resize((180, 100), Image.ANTIALIAS) # ajustar o tamanho da imagem
    photoDistribuicao = ImageTk.PhotoImage(photoDistribuicao)

    photoreposicao = Image.open("reposicao.jpg")
    photoreposicao = photoreposicao.resize((180, 100), Image.ANTIALIAS) # ajustar o tamanho da imagem
    photoreposicao = ImageTk.PhotoImage(photoreposicao)

    photoEnderecamento = Image.open("buscar_endereco.jpg")
    photoEnderecamento = photoEnderecamento.resize((180, 100), Image.ANTIALIAS) # ajustar o tamanho da imagem
    photoEnderecamento = ImageTk.PhotoImage(photoEnderecamento)

    photoUsuario = Image.open("cadUsuario.jpg")
    photoUsuario = photoUsuario.resize((180, 100), Image.ANTIALIAS) # ajustar o tamanho da imagem
    photoUsuario = ImageTk.PhotoImage(photoUsuario)

    photoSeparacao = Image.open("separacao1.jpg")
    photoSeparacao = photoSeparacao.resize((180, 100), Image.ANTIALIAS)  # ajustar o tamanho da imagem
    photoSeparacao = ImageTk.PhotoImage(photoSeparacao)

    # Criar estilo personalizado com um layout vazio para o botão
    style = ttk.Style()
    style.configure('Hidden.TButton', padding=0, relief='flat', background='royalblue', layout=[], font=fonte_Label)



    # Cria o botão com a imagem
    botaoDistribuicao = ttk.Button(TelaBaixo, image=photoDistribuicao, command=lambda: TelaSeparacaoRetorna.FuncaoListaPedidos(TelaInicial))

    botaoreposicao = ttk.Button(TelaBaixo, image=photoreposicao, command=lambda: TelaReposicao.FuncaoReposicao(TelaInicial))

    botaoEnderecamento = ttk.Button(TelaBaixo, image=photoEnderecamento, command=lambda: Tela_Consultar_Enderecos.FuncaoConsultaEnderecos(TelaInicial))

    botaoUsuario = ttk.Button(TelaBaixo, image=photoUsuario, command=lambda: Tela_Cad_Usuario.Funcao_Cadastro(TelaInicial),style='Hidden.TButton')

    botaoSeparacao = ttk.Button(TelaBaixo, image=photoSeparacao)


    def VerificaNome (event):
        CapturarCodigo = Entry_Nome.get()
        if not CapturarCodigo:
            UsuarioNaoEncontrado()
            Entry_Nome.delete(0, END)
            Entry_Nome.focus_set()
        else:
            if not CapturarCodigo.isdigit():
                UsuarioComLetra()
                Entry_Nome.delete(0, END)
                Entry_Nome.focus_set()
            else:
                CapturarNome = Funcoes.PesquisaNomeColaboradorAtivo("ATIVO", CapturarCodigo)
                if not CapturarNome:
                    UsuarioNaoEncontrado()
                    Entry_Nome.delete(0, END)
                    Entry_Nome.focus_set()
                else:
                    Entry_Senha.focus_set()

    Entry_Nome.bind("<Return>", VerificaNome)


    def VerificaSenha (event):
        CapturarCodigo = Entry_Nome.get()
        if not CapturarCodigo:
            UsuarioNaoEncontrado()
            Entry_Senha.delete(0, END)
            Entry_Nome.focus_set()
        else:
            CapturarSenha = Funcoes.PesquisaSenhaColaborador2("ATIVO", CapturarCodigo)
            CapturaraSenha1 = Entry_Senha.get()
            if CapturaraSenha1 != CapturarSenha or not CapturaraSenha1:
                SenhaNaoEncontrado()
                Entry_Senha.delete(0, END)
                Entry_Senha.focus_set()
            else:
                botaoACESSAR.focus_set()

    Entry_Senha.bind("<Return>", VerificaSenha)


    def Acessar():
        CapturarCodigo = Entry_Nome.get()
        CapturarSenha = Entry_Senha.get()
        if not CapturarCodigo and not CapturarSenha:
            mudarCor()
            Entry_Nome.delete(0, END)
            Entry_Senha.delete(0, END)
            Entry_Nome.focus_set()
        else:
            CapturarNome = Funcoes.PesquisaNomeColaboradorAtivo("ATIVO", CapturarCodigo)
            if not CapturarNome:
                UsuarioNaoEncontrado()
                Entry_Nome.delete(0, END)
                Entry_Senha.delete(0, END)
                Entry_Nome.focus_set()
            else:
                Entry_Senha.focus_set()
                CapturaraSenha1 = Entry_Senha.get()
                CapturarSenha2 = Funcoes.PesquisaSenhaColaborador2("ATIVO", CapturarCodigo)
                if CapturaraSenha1 != CapturarSenha2:
                    SenhaNaoEncontrado()
                    Entry_Senha.delete(0, END)
                    Entry_Senha.focus_set()
                else:
                    ValidacaoPermissao = Funcoes.PesquisaPermissaoColaborador("ATIVO", CapturarCodigo)
                    if ValidacaoPermissao == 'ADMINISTRADOR':
                        botaoEnderecamento.pack(side='left', anchor=NW, padx=(100, 0), pady=(0, 0))
                        botaoEnderecamento.config(cursor='hand2')
                        botaoreposicao.pack(side='left', anchor=NW, padx=(100, 0), pady=(0, 0))
                        botaoreposicao.config(cursor='hand2')
                        botaoDistribuicao.pack(side='left', anchor=NW, padx=(100, 0), pady=(0, 0))
                        botaoDistribuicao.config(cursor='hand2')
                        botaoSeparacao.pack(side='left', anchor=NW, padx=(100, 0), pady=(0, 0))
                        botaoSeparacao.config(cursor='hand2')
                        botaoUsuario.pack(side='left', anchor=NW, padx=(100,0),pady=(0,0))
                        botaoUsuario.config(cursor='hand2')
                        labelNomeUsuario.pack(side='left', anchor='e', pady=0, padx=(400,0))
                        labelNomeUsuario.config(text=UsandoGlobal())
                        botaoSair.pack(side='left', anchor='e', pady=0, padx=0)
                        Entry_Nome.pack_forget()
                        Entry_Senha.pack_forget()
                        labelERRO.pack_forget()
                        labelNomeLogin.pack_forget()
                        labelSenhaLogin.pack_forget()
                        botaoACESSAR.pack_forget()
                        globalusuario()

                    else:
                        botaoEnderecamento.pack(side='left', anchor=NW, padx=(400, 0), pady=(0, 0))
                        botaoEnderecamento.config(cursor='hand2')
                        botaoreposicao.pack(side='left', anchor=NW, padx=(100, 0), pady=(0, 0))
                        botaoreposicao.config(cursor='hand2')
                        botaoSeparacao.pack(side='left', anchor=NW, padx=(100, 0), pady=(0, 0))
                        botaoSeparacao.config(cursor='hand2')
                        labelNomeUsuario.pack(side='left', anchor='e', pady=0, padx=(400,0))
                        labelNomeUsuario.config(text=UsandoGlobal())
                        botaoSair.pack(side='left', anchor='e', pady=0, padx=0)
                        Entry_Nome.pack_forget()
                        Entry_Senha.pack_forget()
                        labelERRO.pack_forget()
                        labelNomeLogin.pack_forget()
                        labelSenhaLogin.pack_forget()
                        botaoACESSAR.pack_forget()
                        globalusuario()


    def globalusuario ():
        CapturarCodigo = Entry_Nome.get()
        global usuario
        usuario = CapturarCodigo
        int(usuario)
        return usuario




    botaoACESSAR = ttk.Button(TelaLista2, text='Acessar', command=Acessar,style='Hidden.TButton'  )
    botaoACESSAR.pack( side='top', anchor='center', fill='none', pady=50)
    botaoACESSAR.config(cursor='hand2')

    def voltar ():
        labelNomeLogin.pack(side='top', padx=(0, 0), pady=(10, 0), anchor='e')

        labelSenhaLogin.pack(side='top', padx=(0, 0), pady=(20, 0), anchor='e')

        Entry_Nome.pack(side='top', padx=(0, 0), pady=(10, 0), anchor='w')

        Entry_Senha.pack(side='top', padx=(0, 0), pady=(20, 0), anchor='w')

        labelERRO.pack(side='bottom', anchor='center', padx=(10, 0), pady=(10, 0))

        botaoACESSAR.pack(side='top', anchor='center', fill='none', pady=50)

        botaoDistribuicao.pack_forget()

        botaoSeparacao.pack_forget()

        botaoreposicao.pack_forget()

        botaoEnderecamento.pack_forget()

        botaoUsuario.pack_forget()

        botaoSair.pack_forget()

        labelNomeUsuario.pack_forget()

        Entry_Nome.delete(0, END)
        Entry_Senha.delete(0, END)
        Entry_Nome.focus_set()

    botaoSair = ttk.Button(BordaCima, text='Sair', command=voltar)
    botaoSair.pack_forget()
    botaoSair.config(cursor='hand2')


    def UsandoGlobal():
        CapturarNome = Funcoes.PesquisaNomeColaborador(globalusuario())
        print(CapturarNome)
        return CapturarNome

    labelNomeUsuario = tk.Label(BordaCima, text='', width=25)
    labelNomeUsuario.pack_forget()





    TelaInicial.mainloop()



#ConexaoTags.ConexaoTAGS()
