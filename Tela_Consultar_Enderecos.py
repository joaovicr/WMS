import psutil
import tkinter as tk
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import openpyxl


import Funcoes


def FuncaoConsultaEnderecos(TelaPrincipal):
    TelaPrincipal.update()
    Tela_Consulta_Enderecos = tk.Toplevel(TelaPrincipal)
    Tela_Consulta_Enderecos.title("CONSULTA ENDEREÇOS")
    Tela_Consulta_Enderecos.state("zoomed")
    Tela_Consulta_Enderecos.grab_set()




    # CRIANDO OS FRAMES

    BordaCima = tk.Frame(Tela_Consulta_Enderecos, width=50, height=25, bg="royalblue")
    BordaCima.pack(side="top", fill="both", expand=False)

    Corpo = tk.Frame(Tela_Consulta_Enderecos, width=500, height=900, bg="white")
    Corpo.pack(side="top", fill="both", expand=True)

    CorpoCima = tk.Frame(Corpo, width=500, height=250, bg="gray")
    CorpoCima.pack(side="top", fill="both", expand=False)

    CorpoCima1_1 = tk.Frame(CorpoCima, width=250, height=250, bg="gray")
    CorpoCima1_1.pack(side="left", fill="both", expand=True)

    CorpoCima1_2 = tk.Frame(CorpoCima, width=250, height=250, bg="gray")
    CorpoCima1_2.pack(side="left", fill="both", expand=True)

    CorpoBaixo = tk.Frame(Corpo, width=500, height=650, bg="gray")
    CorpoBaixo.pack(side="top", fill="both", expand=True)

    CorpoBaixo1_1 = tk.Frame(CorpoBaixo, width=200, height=650, bg="gray")
    CorpoBaixo1_1.pack(side="left", fill="both", expand=True)

    CorpoBaixo1_2 = tk.Frame(CorpoBaixo, width=100, height=650, bg="gray")
    CorpoBaixo1_2.pack(side="left", fill="both", expand=False)

    CorpoBaixo1_3 = tk.Frame(CorpoBaixo, width=50, height=650, bg="gray")
    CorpoBaixo1_3.pack(side="left", fill="both", expand=False)

    CorpoBaixo1_4 = tk.Frame(CorpoBaixo, width=150, height=650, bg="gray")
    CorpoBaixo1_4.pack(side="left", fill="both", expand=True)


    fonte_Titulo = Font(size=26, family="Rockwell", weight="bold")
    fonte_Label = Font(size=22, family="Rockwell", weight="bold")
    fonte_Entry = Font(size=22, family="Rockwell", weight="bold")
    fonte_Listbox = Font(size=14, family="Rockwell", weight="bold")



    # CRIANDO AS LABELS
    label_Titulo_Tela = tk.Label(BordaCima, text="CONSULTA DE ENDEREÇOS", bg="royalblue", font=fonte_Titulo)
    label_Titulo_Tela.pack()

    Label_Tag = tk.Label(CorpoCima1_1, text="INSIRA O ITEM:", width=15, bg="GRAY", foreground="white", font=fonte_Label)

    Label_Referencia = tk.Label(CorpoBaixo1_1, text="REFERÊNCIA:", width=11, bg="GRAY", foreground="white", font=fonte_Listbox)

    Label_Endereco = tk.Label(CorpoBaixo1_3, text="ENDEREÇOS:", width=10, bg="GRAY", foreground="white", font=fonte_Listbox)

    Label_Descricao = tk.Label(CorpoBaixo1_2, text="DESCRIÇÃO ITEM:", width=15, bg="GRAY", foreground="white", font=fonte_Listbox)


    Listbox_Retorna_Engenharia = Listbox(CorpoBaixo1_1, width=16, bg="GRAY", foreground="black", font=fonte_Listbox)

    Listbox_Endereço = Listbox(CorpoBaixo1_3, width=17, bg="GRAY", foreground="black", font=fonte_Listbox)

    Listbox_Descricao = Listbox(CorpoBaixo1_2, width=60, bg="GRAY", foreground="black", font=fonte_Listbox)



    # CRIANDO AS ENTRY'S
    Entry_Tag = tk.Entry(CorpoCima1_2, width=20, font=fonte_Entry, borderwidth=2)
    Entry_Tag.delete(0, END)
    Entry_Tag.focus_set()





    def Retorna_Reduzido(event):
        CapturarTag = Entry_Tag.get()
        CapturarTag = str(CapturarTag)
        Reduzido = Funcoes.Pesquisa_Reduzido(CapturarTag)
        Engenharia = Funcoes.Pesquisa_Engenharia_Engenharia(CapturarTag)
        Reduzido1 = Funcoes.Pesquisa_Engenharia_Reduzido(CapturarTag)

        if not CapturarTag:
            tela_msgbox = tk.Toplevel(Tela_Consulta_Enderecos)
            tela_msgbox.overrideredirect(True)
            tela_msgbox.geometry('0x0+{}+{}'.format(900, 500))
            tela_msgbox.title("Mensagem")
            messagebox.showerror("CAMPO VAZIO", "Por favor, Insira um código válido.".format(CapturarTag),
                                parent=tela_msgbox)
            tela_msgbox.destroy()

        else:
            if not Reduzido1 and not Engenharia and not Reduzido:
                tela_msgbox1 = tk.Toplevel(Tela_Consulta_Enderecos)
                tela_msgbox1.overrideredirect(True)
                tela_msgbox1.geometry('0x0+{}+{}'.format(900, 500))
                tela_msgbox1.title("Mensagem")
                messagebox.showerror("Item não Possui Endereço", "Por favor, Insira um Item válido.".format(CapturarTag),
                                     parent=tela_msgbox1)
                tela_msgbox1.destroy()
                Entry_Tag.delete(0, END)
                Entry_Tag.focus_set()
            else:
                if len(CapturarTag) == 6:
                    endereco = Funcoes.Pesquisa_Endereco_Reduzido(CapturarTag)
                    Engenharia = Funcoes.Pesquisa_Engenharia_Reduzido(CapturarTag)
                    Descricao = Funcoes.Pesquisa_Descricao_Reduzido(CapturarTag)
                    for end in endereco:
                        Listbox_Endereço.insert(END, end)
                    for eng in Engenharia:
                        Listbox_Retorna_Engenharia.insert(END, eng)
                    for des in Descricao:
                        Listbox_Descricao.insert(END, des)
                        Entry_Tag.delete(0, END)
                        Entry_Tag.focus_set()

                elif len(CapturarTag) == 8:
                    endereco = Funcoes.Pesquisa_Endereco_Engenharia(CapturarTag)
                    Engenharia = Funcoes.Pesquisa_Engenharia_Engenharia(CapturarTag)
                    Descricao = Funcoes.Pesquisa_Descricao_Engenharia(CapturarTag)
                    for end in endereco:
                        Listbox_Endereço.insert(END, end)
                    for eng in Engenharia:
                        Listbox_Retorna_Engenharia.insert(END, eng)
                    for des in Descricao:
                        Listbox_Descricao.insert(END, des)
                        Entry_Tag.delete(0, END)
                        Entry_Tag.focus_set()

                elif len(CapturarTag) > 10:
                    endereco = Funcoes.Pesquisa_Endereco_Reduzido(Reduzido)
                    Engenharia = Funcoes.Pesquisa_Engenharia_Reduzido(Reduzido)
                    Descricao = Funcoes.Pesquisa_Descricao_Reduzido(Reduzido)
                    for end in endereco:
                        Listbox_Endereço.insert(END, end)
                    for eng in Engenharia:
                        Listbox_Retorna_Engenharia.insert(END, eng)
                    for des in Descricao:
                        Listbox_Descricao.insert(END, des)
                        Entry_Tag.delete(0, END)
                        Entry_Tag.focus_set()


    Entry_Tag.bind("<Return>", Retorna_Reduzido)


    def limpar_itens():
        Listbox_Retorna_Engenharia.delete(0, tk.END)
        Listbox_Endereço.delete(0, tk.END)
        Listbox_Descricao.delete(0, tk.END)
        Entry_Tag.delete(0, END)
        Entry_Tag.focus_set()

    def enviar_Excel():
        Engenharia = Listbox_Retorna_Engenharia.get(0, tk.END)
        Descricao = Listbox_Descricao.get(0, tk.END)
        Enderecos = Listbox_Endereço.get(0, tk.END)


        Uniao = list(filter(lambda x: len(x) > 1, zip(Engenharia, Descricao, Enderecos)))

        Uniao = [[str(cell).strip("('").strip("',)") for cell in row] for row in Uniao]

        filename = 'Enderecamento.xlsx'

        for proc in psutil.process_iter():
            try:
                # Verifica se o nome do arquivo está na linha de comando do processo
                if filename in ' '.join(proc.cmdline()):
                    # Fecha o processo
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass


        try:

            wb = openpyxl.Workbook()
            ws = wb.active

            header = ('Engenharia', 'Descrição', 'Endereço')
            ws.append(header)

            for row in Uniao:
                ws.append(row)

            wb.save(filename)

            messagebox.showinfo('Exportar para Excel', f'Dados exportados para {filename} com sucesso.')

            os.startfile('Enderecamento.xlsx')

        except Exception as e:
            messagebox.showerror('Exportar para Excel', f'Erro ao exportar dados: Favor fechar a planilha primeiro')



    photosalvar = Image.open("exportar_excel.jpg")
    photosalvar = photosalvar.resize((50, 50), Image.ANTIALIAS)  # ajustar o tamanho da imagem
    photosalvar = ImageTk.PhotoImage(photosalvar)


    botao_exportar = Button(CorpoBaixo1_4, image=photosalvar, command= enviar_Excel)
    Entry_Tag.focus_set()

    photoLimparFiltros = Image.open("limpar_filtros.jpg")
    photoLimparFiltros = photoLimparFiltros.resize((50, 50), Image.ANTIALIAS)  # ajustar o tamanho da imagem
    photoLimparFiltros = ImageTk.PhotoImage(photoLimparFiltros)

    botaoLimparFiltros = Button(CorpoBaixo1_4, image=photoLimparFiltros, command=limpar_itens)
    Entry_Tag.focus_set()

    Label_Tag.pack(side='top', anchor=SE, padx=(0, 0), pady=(100, 0))
    Entry_Tag.pack(side='top', anchor=W, pady= 100, padx = 5)
    Label_Referencia.pack(side='top', anchor=NE, pady= 0, padx = 15)
    Label_Descricao.pack(side='top', anchor=NW, pady=0, padx=(230,0))
    Label_Endereco.pack(side='top', anchor=NW, pady= 0, padx = 30)
    Listbox_Retorna_Engenharia.pack(side='top', anchor=NE, pady= 5, padx = 0)
    Listbox_Descricao.pack(side='top', anchor=NW, pady=5, padx=10)
    Listbox_Endereço.pack(side='top', anchor=NW, pady= 5, padx = 10)
    botao_exportar.pack(side='bottom', anchor=SE, pady= 10, padx = 10)
    botaoLimparFiltros.pack(side='bottom', anchor=SE, pady=10, padx=10)






    Tela_Consulta_Enderecos.protocol("WM_DELETE_WINDOW", lambda: voltar_tela1(TelaPrincipal, Tela_Consulta_Enderecos))

    def voltar_tela1(TelaPrincipal, Tela_Consulta_Enderecos):
        # reabilita a tela1
        TelaPrincipal.deiconify()
        TelaPrincipal.state('zoomed')
        Tela_Consulta_Enderecos.destroy()



    Tela_Consulta_Enderecos.wait_window()

