#imports 
#maybe you should download some of libraries bellow using pip
import sys

from tkinter import Image, StringVar

from PIL import Image, ImageTk 
import time

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import os.path


#Stating class and first window 

#class Toplevel1 (application)
class Toplevel1:
        def __init__(self):
                #first window
                _bgcolor = '#d9d9d9'  # X11 color: 'gray85' --> Cinza85
                _fgcolor = '#000000'  # X11 color: 'black' --> Preto
                _compcolor = '#d9d9d9' # X11 color: 'gray85' --> Cinza85
                _ana1color = '#d9d9d9' # X11 color: 'gray85' --> Cinza85
                _ana2color = '#ececec' # Closest X11 color: 'gray92' --> Cinza92
                font10 = "-family {Segoe UI} -size 20 -weight bold" #fonte Seoge UI weigth 20, bold
                font9 = "-family {Segoe UI} -size 24 -weight bold" #fonte Seoge UI weigth 24, bold
                font8 = "-family {Segoe UI} -size 14 -weight bold" #font Seoge UI weigth 14, bold

                self.top=tk.Tk()
                self.top.title('Colinas Magazine') #Títuto
          
                self.top.resizable(0, 0) #janela irredimensionável 
                self.top.configure(background="#ffffff") #Cor de fundo da janela: Branco
                self.top.attributes('-fullscreen', True) #Colocando janela em fullscreen(tela cheia)

                '''Barra do topo'''
                self.topbar = tk.Frame(self.top) 
                self.topbar.place(relx=-0.007, rely=0.0, relheight=0.101, relwidth=1.015) #posicionamento

                self.topbar.configure(relief='flat') #Borda
                self.topbar.configure(borderwidth="2") #tamanho da borda
                self.topbar.configure(background="#0995FE") #Cor de fundo --> Cinza
                self.topbar.configure(highlightbackground="#d9d9d9") #Contraste fundo -->Cinza
                self.topbar.configure(highlightcolor="black") #Contraste -->Preto

                '''LOGO'''
                self.logo = tk.Label(self.topbar)
                self.logo.place(relx=0.007, rely=0.133, height=61, width=94) #posicionamento
                self.logo.configure(background="#d9d9d9") #Cord do fundo -->Cinza
                self.logo.configure(disabledforeground="#a3a3a3") #Cor do fundo -->Azulzinho que não qual a tonalidade
                logo = tk.PhotoImage(file="C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\logo.png") #Variável com nome do aqruivo
                self.logo.configure(image=logo) #chamando a imagem
        
                '''Carrinho'''
                self.btncarrinho = tk.Button(self.topbar) #Botão carrinho de compras
                self.btncarrinho.place(relx=0.923, rely=0.0, height=74, width=96) #posicionamento
                self.btncarrinho.configure(activebackground="#ececec") #fundo ativo
                self.btncarrinho.configure(background="#d9d9d9") #Cor de fundo
                self.btncarrinho.configure(highlightbackground="#d9d9d9") #Contraste fundo
                self.btncarrinho.configure(command=self.janela3)

                carrinho = tk.PhotoImage(file="C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\carrinho.png") #variável com o arquivo 
                self.btncarrinho.configure(image=carrinho) #chamando a variável
                self.btncarrinho.configure(relief='flat') #Borda
                self.btncarrinho.configure(cursor='hand2') #Cursor
                
                '''Nome da Loja'''
                self.Nomeloja = tk.Label(self.topbar) #label
                self.Nomeloja.place(relx=0.072, rely=0.0, height=81, width=283) #posicionamento
                self.Nomeloja.configure(background="#0995FE") #cor de fundo --> Azul
                self.Nomeloja.configure(disabledforeground="#a3a3a3") 
                self.Nomeloja.configure(font=font9) #fonte
                self.Nomeloja.configure(foreground="#ffffff") #cor
                self.Nomeloja.configure(justify='right') #justificar
                self.Nomeloja.configure(text='''Colinas Magazine''') #Texto

                '''Primeiro frame, botão, imagem, Nome do produto e descrição''' # 1° FRAME
                self.Frame1 = tk.Frame(self.top)
                self.Frame1.place(relx=0.007, rely=0.121, relheight=0.409, relwidth=0.179) #posicionamento
                self.Frame1.configure(relief='flat') #borda
                self.Frame1.configure(borderwidth="2") #tamanho da borda
                self.Frame1.configure(background="#d9d9d9") #Cor de fundo --> Azul

                self.Button1 = tk.Button(self.Frame1)
                self.Button1.place(relx=0.779, rely=0.82, height=44, width=46) #posicionamento
                self.Button1.configure(activebackground="#ececec")
                self.Button1.configure(activeforeground="#000000")
                self.Button1.configure(background="#d9d9d9")
                self.Button1.configure(disabledforeground="#a3a3a3")
                self.Button1.configure(foreground="#000000")
                self.Button1.configure(highlightbackground="#d9d9d9")
                self.Button1.configure(highlightcolor="black") 
                bt1 = tk.PhotoImage(file="C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\btn.png") #Arquivo
                self.Button1.configure(image=bt1) #chamando o arquivo
                self.Button1.configure(relief='flat') #borda
                self.Button1.configure(cursor='hand2') #cursor
                self.Button1.configure(command=botao1) #comando do botão


                self.Label1 = tk.Label(self.Frame1)
                self.Label1.place(relx=0.0, rely=0.689, height=51, width=144)
                self.Label1.configure(background="#d9d9d9")
                self.Label1.configure(disabledforeground="#a3a3a3")
                self.Label1.configure(font=font10)
                self.Label1.configure(foreground="#000000")
                self.Label1.configure(justify='right')
                self.Label1.configure(text='Smart TV')

                self.desc1 = tk.Label(self.Frame1)
                self.desc1.place(relx=0.041, rely=0.852, height=21, width=124)
                self.desc1.configure(background="#d9d9d9")
                self.desc1.configure(disabledforeground="#a3a3a3")
                self.desc1.configure(foreground="#0995FE")
                self.desc1.configure(text='R$2700,00')
                self.desc1.configure(anchor='w', font=font8)

                #IMAGEM DO PRODUTO
                self.imagem1 = tk.Label(self.Frame1)
                self.imagem1.place(relx=0.081, rely=0.066, height=191, width=200)
                self.imagem1.configure(background="#d9d9d9")
                self.imagem1.configure(disabledforeground="#a3a3a3")
                img1 = tk.PhotoImage(file='C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\tv.png')
                self.imagem1.configure(image=img1)
        
                self.menubar = tk.Menu(self.top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
                self.top.configure(menu = self.menubar)

                '''Obs: A partir daqui as configurações serão as mesmas para os elementos, 
                porém não vou comentar pois os elementos são os mesmos
                (como se fossem cópias), só muda a posição'''

                '''Segundo frame, botão, imagem, Nome do produto e descrição''' # 2° FRAME
                self.Frame2 = tk.Frame(self.top)
                self.Frame2.place(relx=0.205, rely=0.121, relheight=0.409, relwidth=0.179)
                self.Frame2.configure(relief='flat')
                self.Frame2.configure(borderwidth="2")
                self.Frame2.configure(background="#d9d9d9")
                self.Frame2.configure(highlightbackground="#d9d9d9")
                self.Frame2.configure(highlightcolor="black")

                self.Button2 = tk.Button(self.Frame2)
                self.Button2.place(relx=0.776, rely=0.82, height=44, width=46)
                self.Button2.configure(activebackground="#ececec")
                self.Button2.configure(activeforeground="#000000")
                self.Button2.configure(background="#d9d9d9")
                self.Button2.configure(disabledforeground="#a3a3a3")
                self.Button2.configure(foreground="#000000")
                self.Button2.configure(highlightbackground="#d9d9d9")
                self.Button2.configure(highlightcolor="black")
                self.Button2.configure(image=bt1)
                self.Button2.configure(relief='flat') 
                self.Button2.configure(cursor='hand2')
                self.Button2.configure(command=botao2)
        
                self.Label2 = tk.Label(self.Frame2)
                self.Label2.place(relx=0.02, rely=0.689, height=51, width=144)
                self.Label2.configure(activebackground="#f9f9f9")
                self.Label2.configure(activeforeground="black")
                self.Label2.configure(background="#d9d9d9")
                self.Label2.configure(disabledforeground="#a3a3a3")
                self.Label2.configure(font="-family {Segoe UI} -size 20 -weight bold")
                self.Label2.configure(foreground="#000000")
                self.Label2.configure(highlightbackground="#d9d9d9")
                self.Label2.configure(highlightcolor="black")
                self.Label2.configure(justify='right')
                self.Label2.configure(text='Lava e seca')

                self.desc2 = tk.Label(self.Frame2)
                self.desc2.place(relx=0.02, rely=0.852, height=21, width=124)
                self.desc2.configure(activebackground="#f9f9f9")
                self.desc2.configure(activeforeground="black")
                self.desc2.configure(background="#d9d9d9")
                self.desc2.configure(foreground="#0995FE")
                self.desc2.configure(text='R$3699,00')
                self.desc2.configure(font=font8, anchor='w')
  
                #IMAGEM DO PRODUTO
                self.imagem2 = tk.Label(self.Frame2)
                self.imagem2.place(relx=0.082, rely=0.066, height=191, width=194)
                self.imagem2.configure(background="#d9d9d9")
                self.imagem2.configure(disabledforeground="#a3a3a3")
                img2 = tk.PhotoImage(file='C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\lavadeira.png')
                self.imagem2.configure(image=img2)

                '''Terceiro frame, botão, imagem, Nome do produto e descrição''' # 3° FRAME
                self.Frame3 = tk.Frame(self.top)
                self.Frame3.place(relx=0.403, rely=0.121, relheight=0.409, relwidth=0.179)
                self.Frame3.configure(relief='flat')
                self.Frame3.configure(borderwidth="2")
                self.Frame3.configure(background="#d9d9d9")
                self.Frame3.configure(highlightbackground="#d9d9d9")
                self.Frame3.configure(highlightcolor="black")

                self.Button3 = tk.Button(self.Frame3)
                self.Button3.place(relx=0.776, rely=0.82, height=44, width=46)
                self.Button3.configure(activebackground="#ececec")
                self.Button3.configure(activeforeground="#000000")
                self.Button3.configure(background="#d9d9d9")
                self.Button3.configure(disabledforeground="#a3a3a3")
                self.Button3.configure(foreground="#000000")
                self.Button3.configure(highlightbackground="#d9d9d9")
                self.Button3.configure(highlightcolor="black")
                self.Button3.configure(image=bt1)
                self.Button3.configure(relief='flat') 
                self.Button3.configure(cursor='hand2')
                self.Button3.configure(command=botao3)

                self.Label3 = tk.Label(self.Frame3)
                self.Label3.place(relx=0.033, rely=0.689, height=51, width=144)
                self.Label3.configure(activebackground="#f9f9f9")
                self.Label3.configure(activeforeground="black")
                self.Label3.configure(background="#d9d9d9")
                self.Label3.configure(disabledforeground="#a3a3a3")
                self.Label3.configure(font="-family {Segoe UI} -size 20 -weight bold")
                self.Label3.configure(foreground="#000000")
                self.Label3.configure(highlightbackground="#d9d9d9")
                self.Label3.configure(highlightcolor="black")
                self.Label3.configure(justify='right')
                self.Label3.configure(text='Iphone 12')

                self.desc3 = tk.Label(self.Frame3)
                self.desc3.place(relx=0.041, rely=0.852, height=21, width=124)
                self.desc3.configure(activebackground="#f9f9f9")
                self.desc3.configure(activeforeground="black")
                self.desc3.configure(background="#d9d9d9")
                self.desc3.configure(disabledforeground="#a3a3a3")
                self.desc3.configure(foreground="#0995FE")
                self.desc3.configure(text='R$7029,00')
                self.desc3.configure(anchor='w', font=font8)

                #IMAGEM DO PRODUTO
                self.imagem3 = tk.Label(self.Frame3)
                self.imagem3.place(relx=0.082, rely=0.066, height=191, width=194)
                self.imagem3.configure(background="#d9d9d9")
                self.imagem3.configure(disabledforeground="#a3a3a3")
                img3 = tk.PhotoImage(file='C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\celular.png')
                self.imagem3.configure(image=img3)

                '''Quarto frame, botão, imagem, Nome do produto e descrição''' # 4° FRAME
                self.Frame4 = tk.Frame(self.top)
                self.Frame4.place(relx=0.6, rely=0.121, relheight=0.409, relwidth=0.187)
                self.Frame4.configure(relief='flat')
                self.Frame4.configure(borderwidth="2")
                self.Frame4.configure(background="#d9d9d9")
                self.Frame4.configure(highlightbackground="#d9d9d9")
                self.Frame4.configure(highlightcolor="black")

                self.Button4 = tk.Button(self.Frame4)
                self.Button4.place(relx=0.784, rely=0.82, height=44, width=46)
                self.Button4.configure(activebackground="#ececec")
                self.Button4.configure(activeforeground="#000000")
                self.Button4.configure(background="#d9d9d9")
                self.Button4.configure(disabledforeground="#a3a3a3")
                self.Button4.configure(foreground="#000000")
                self.Button4.configure(highlightbackground="#d9d9d9")
                self.Button4.configure(highlightcolor="black")
                self.Button4.configure(image=bt1)
                self.Button4.configure(relief='flat') 
                self.Button4.configure(cursor='hand2')
                self.Button4.configure(command=botao4)

                self.Label4 = tk.Label(self.Frame4)
                self.Label4.place(relx=0.02, rely=0.689, height=51, width=170)
                self.Label4.configure(activebackground="#f9f9f9")
                self.Label4.configure(activeforeground="black")
                self.Label4.configure(background="#d9d9d9")
                self.Label4.configure(disabledforeground="#a3a3a3")
                self.Label4.configure(font="-family {Segoe UI} -size 17 -weight bold")
                self.Label4.configure(foreground="#000000")
                self.Label4.configure(highlightbackground="#d9d9d9")
                self.Label4.configure(highlightcolor="black")
                self.Label4.configure(justify='right')
                self.Label4.configure(text='Fone Bluetooth')

                self.desc4 = tk.Label(self.Frame4)
                self.desc4.place(relx=0.02, rely=0.852, height=21, width=124)
                self.desc4.configure(activebackground="#f9f9f9")
                self.desc4.configure(activeforeground="black")
                self.desc4.configure(background="#d9d9d9")
                self.desc4.configure(disabledforeground="#a3a3a3")
                self.desc4.configure(foreground="#0995FE")
                self.desc4.configure(text='R$197,91')
                self.desc4.configure(anchor='w', font=font8)

                #IMAGEM DO PRODUTO
                self.imagem4 = tk.Label(self.Frame4)
                self.imagem4.place(relx=0.0, rely=0.066, height=191, width=238)
                self.imagem4.configure(background="#d9d9d9")
                self.imagem4.configure(disabledforeground="#a3a3a3")
                img4 = tk.PhotoImage(file='C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\airpods.png')
                self.imagem4.configure(image=img4)

                '''Quinto frame, botão, imagem, Nome do produto e descrição''' # 5° FRAME
                self.Frame5 = tk.Frame(self.top)
                self.Frame5.place(relx=0.805, rely=0.121, relheight=0.409, relwidth=0.179)
                self.Frame5.configure(relief='flat')
                self.Frame5.configure(borderwidth="2")
                self.Frame5.configure(background="#d9d9d9")
                self.Frame5.configure(highlightbackground="#d9d9d9")
                self.Frame5.configure(highlightcolor="black")

                self.Button5 = tk.Button(self.Frame5)
                self.Button5.place(relx=0.784, rely=0.82, height=44, width=46)
                self.Button5.configure(activebackground="#ececec")
                self.Button5.configure(activeforeground="#000000")
                self.Button5.configure(background="#d9d9d9")
                self.Button5.configure(disabledforeground="#a3a3a3")
                self.Button5.configure(foreground="#000000")
                self.Button5.configure(highlightbackground="#d9d9d9")
                self.Button5.configure(highlightcolor="black")
                self.Button5.configure(image=bt1)
                self.Button5.configure(relief='flat') 
                self.Button5.configure(cursor='hand2')
                self.Button5.configure(command=botao5)

                self.Label5 = tk.Label(self.Frame5)
                self.Label5.place(relx=0.0, rely=0.689, height=51, width=144)
                self.Label5.configure(activebackground="#f9f9f9")
                self.Label5.configure(activeforeground="black")
                self.Label5.configure(background="#d9d9d9")
                self.Label5.configure(disabledforeground="#a3a3a3")
                self.Label5.configure(font="-family {Segoe UI} -size 20 -weight bold")
                self.Label5.configure(foreground="#000000")
                self.Label5.configure(highlightbackground="#d9d9d9")
                self.Label5.configure(highlightcolor="black")
                self.Label5.configure(justify='right')
                self.Label5.configure(text='Cooktop')

                self.desc5 = tk.Label(self.Frame5)
                self.desc5.place(relx=0.065, rely=0.852, height=21, width=124)
                self.desc5.configure(activebackground="#f9f9f9")
                self.desc5.configure(activeforeground="black")
                self.desc5.configure(background="#d9d9d9")
                self.desc5.configure(disabledforeground="#a3a3a3")
                self.desc5.configure(foreground="#0995FE")
                self.desc5.configure(text='R$581,83')
                self.desc5.configure(anchor='w', font=font8)

                #IMAGEM DO PRODUTO
                self.imagem5 = tk.Label(self.Frame5)
                self.imagem5.place(relx=0.118, rely=0.033, height=191, width=194)
                self.imagem5.configure(background="#d9d9d9")
                self.imagem5.configure(disabledforeground="#a3a3a3")
                img5 = tk.PhotoImage(file='C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\forno.png')
                self.imagem5.configure(image=img5)

                '''Sexto frame, botão, imagem, Nome do produto e descrição''' # 6° FRAME
                self.Frame6 = tk.Frame(self.top)
                self.Frame6.place(relx=0.007, rely=0.55, relheight=0.409, relwidth=0.179)

                self.Frame6.configure(relief='flat')
                self.Frame6.configure(borderwidth="2")
                self.Frame6.configure(background="#d9d9d9")
                self.Frame6.configure(highlightbackground="#d9d9d9")
                self.Frame6.configure(highlightcolor="black")

                self.Button6 = tk.Button(self.Frame6)
                self.Button6.place(relx=0.779, rely=0.82, height=44, width=46)
                self.Button6.configure(activebackground="#ececec")
                self.Button6.configure(activeforeground="#000000")
                self.Button6.configure(background="#d9d9d9")
                self.Button6.configure(disabledforeground="#a3a3a3")
                self.Button6.configure(foreground="#000000")
                self.Button6.configure(highlightbackground="#d9d9d9")
                self.Button6.configure(highlightcolor="black")
                self.Button6.configure(image=bt1)
                self.Button6.configure(relief='flat') 
                self.Button6.configure(cursor='hand2')
                self.Button6.configure(command=botao6)

                self.Label6 = tk.Label(self.Frame6)
                self.Label6.place(relx=0.0, rely=0.721, height=51, width=180)
                self.Label6.configure(activebackground="#f9f9f9")
                self.Label6.configure(activeforeground="black")
                self.Label6.configure(background="#d9d9d9")
                self.Label6.configure(disabledforeground="#a3a3a3")
                self.Label6.configure(font="-family {Segoe UI} -size 17 -weight bold")
                self.Label6.configure(foreground="#000000")
                self.Label6.configure(highlightbackground="#d9d9d9")
                self.Label6.configure(highlightcolor="black")
                self.Label6.configure(justify='right')
                self.Label6.configure(text='Cadeira giratória')

                self.desc6 = tk.Label(self.Frame6)
                self.desc6.place(relx=0.01, rely=0.885, height=21, width=124)
                self.desc6.configure(activebackground="#f9f9f9")
                self.desc6.configure(activeforeground="black")
                self.desc6.configure(background="#d9d9d9")
                self.desc6.configure(foreground="#0995FE")
                self.desc6.configure(text='R$759,98')
                self.desc6.configure(anchor='w', font=font8)

                #IMAGEM DO PRODUTO          
                self.imagem6 = tk.Label(self.Frame6)
                self.imagem6.place(relx=0.082, rely=0.066, height=191, width=204)
                self.imagem6.configure(background="#d9d9d9")
                self.imagem6.configure(disabledforeground="#a3a3a3")
                img6 = tk.PhotoImage(file='C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\cadeira.png')
                self.imagem6.configure(image=img6)

                '''Sétimo frame, botão, imagem, Nome do produto e descrição''' # 7° FRAME
                self.Frame7 = tk.Frame(self.top)
                self.Frame7.place(relx=0.205, rely=0.55, relheight=0.409, relwidth=0.179)

                self.Frame7.configure(relief='flat')
                self.Frame7.configure(borderwidth="2")
                self.Frame7.configure(background="#d9d9d9")
                self.Frame7.configure(highlightbackground="#d9d9d9")
                self.Frame7.configure(highlightcolor="black")

                self.Button7 = tk.Button(self.Frame7)
                self.Button7.place(relx=0.776, rely=0.82, height=46, width=46)
                self.Button7.configure(activebackground="#ececec")
                self.Button7.configure(activeforeground="#000000")
                self.Button7.configure(background="#d9d9d9")
                self.Button7.configure(disabledforeground="#a3a3a3")
                self.Button7.configure(foreground="#000000")
                self.Button7.configure(highlightbackground="#d9d9d9")
                self.Button7.configure(highlightcolor="black")
                self.Button7.configure(image=bt1)
                self.Button7.configure(relief='flat')
                self.Button7.configure(cursor='hand2')
                self.Button7.configure(command=botao7)

                self.Label7 = tk.Label(self.Frame7)
                self.Label7.place(relx=0.0, rely=0.721, height=51, width=190)
                self.Label7.configure(activebackground="#f9f9f9")
                self.Label7.configure(activeforeground="black")
                self.Label7.configure(background="#d9d9d9")
                self.Label7.configure(disabledforeground="#a3a3a3")
                self.Label7.configure(font="-family {Segoe UI} -size 16 -weight bold")
                self.Label7.configure(foreground="#000000")
                self.Label7.configure(highlightbackground="#d9d9d9")
                self.Label7.configure(highlightcolor="black")
                self.Label7.configure(justify='right')
                self.Label7.configure(text='Impressora EPSON', anchor='w')

                self.desc7 = tk.Label(self.Frame7)
                self.desc7.place(relx=0.01, rely=0.885, height=21, width=124)
                self.desc7.configure(activebackground="#f9f9f9")
                self.desc7.configure(activeforeground="black")
                self.desc7.configure(background="#d9d9d9")
                self.desc7.configure(disabledforeground="#a3a3a3")
                self.desc7.configure(foreground="#0995FE")
                self.desc7.configure(text='R$949,85')
                self.desc7.configure(anchor='w', font=font8)

                #IMAGEM DO PRODUTO
                self.imagem7 = tk.Label(self.Frame7)
                self.imagem7.place(relx=0.0, rely=0.066, height=191, width=238)
                self.imagem7.configure(background="#d9d9d9")
                self.imagem7.configure(disabledforeground="#a3a3a3")
                img7 = tk.PhotoImage(file='C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\impressora.png')
                self.imagem7.configure(image=img7)

                '''Oitavo frame, botão, imagem, Nome do produto e descrição''' # 8° FRAME
                self.Frame8 = tk.Frame(self.top)
                self.Frame8.place(relx=0.403, rely=0.55, relheight=0.409, relwidth=0.179)

                self.Frame8.configure(relief='flat')
                self.Frame8.configure(borderwidth="2")
                self.Frame8.configure(background="#d9d9d9")
                self.Frame8.configure(highlightbackground="#d9d9d9")
                self.Frame8.configure(highlightcolor="black")

                self.Button8 = tk.Button(self.Frame8)
                self.Button8.place(relx=0.776, rely=0.82, height=44, width=46)
                self.Button8.configure(activebackground="#ececec")
                self.Button8.configure(activeforeground="#000000")
                self.Button8.configure(background="#d9d9d9")
                self.Button8.configure(disabledforeground="#a3a3a3")
                self.Button8.configure(foreground="#000000")
                self.Button8.configure(highlightbackground="#d9d9d9")
                self.Button8.configure(highlightcolor="black")
                self.Button8.configure(image=bt1)
                self.Button8.configure(relief='flat') 
                self.Button8.configure(cursor='hand2')
                self.Button8.configure(command=botao8)

                self.Label8 = tk.Label(self.Frame8)
                self.Label8.place(relx=0.0, rely=0.721, height=51, width=180)
                self.Label8.configure(activebackground="#f9f9f9")
                self.Label8.configure(activeforeground="black")
                self.Label8.configure(background="#d9d9d9")
                self.Label8.configure(disabledforeground="#a3a3a3")
                self.Label8.configure(font="-family {Segoe UI} -size 17 -weight bold")
                self.Label8.configure(foreground="#000000")
                self.Label8.configure(highlightbackground="#d9d9d9")
                self.Label8.configure(highlightcolor="black")
                self.Label8.configure(justify='right')
                self.Label8.configure(text='Notebook 8gb')

                self.desc8 = tk.Label(self.Frame8)
                self.desc8.place(relx=0.041, rely=0.885, height=21, width=124)
                self.desc8.configure(activebackground="#f9f9f9")
                self.desc8.configure(activeforeground="black")
                self.desc8.configure(background="#d9d9d9")
                self.desc8.configure(foreground="#0995FE")
                self.desc8.configure(text='R$5034,00')
                self.desc8.configure(anchor='w', font=font8)

                #IMAGEM DO PRODUTO
                self.imagem8 = tk.Label(self.Frame8)
                self.imagem8.place(relx=0.082, rely=0.033, height=211, width=204)
                self.imagem8.configure(background="#d9d9d9")
                self.imagem8.configure(disabledforeground="#a3a3a3")
                img8 = tk.PhotoImage(file='C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\notebook.png')
                self.imagem8.configure(image=img8)

                '''Nono frame, botão, imagem, Nome do produto e descrição''' # 9° FRAME
                self.Frame9 = tk.Frame(self.top)
                self.Frame9.place(relx=0.6, rely=0.55, relheight=0.409, relwidth=0.186)
                self.Frame9.configure(relief='flat')
                self.Frame9.configure(borderwidth="2")
                self.Frame9.configure(background="#d9d9d9")
                self.Frame9.configure(highlightbackground="#d9d9d9")
                self.Frame9.configure(highlightcolor="black")

                self.Frame1_9 = tk.Frame(self.Frame9)
                self.Frame1_9.place(relx=3.209, rely=1.318, relheight=1.0, relwidth=1.0)
                self.Frame1_9.configure(relief='flat')
                self.Frame1_9.configure(borderwidth="2")
                self.Frame1_9.configure(background="#d9d9d9")
                self.Frame1_9.configure(highlightbackground="#d9d9d9")
                self.Frame1_9.configure(highlightcolor="black")

                self.Button9 = tk.Button(self.Frame9)
                self.Button9.place(relx=0.787, rely=0.82, height=44, width=46)
                self.Button9.configure(activebackground="#ececec")
                self.Button9.configure(activeforeground="#000000")
                self.Button9.configure(background="#d9d9d9")
                self.Button9.configure(disabledforeground="#a3a3a3")
                self.Button9.configure(foreground="#000000")
                self.Button9.configure(highlightbackground="#d9d9d9")
                self.Button9.configure(highlightcolor="black")
                self.Button9.configure(image=bt1)
                self.Button9.configure(relief='flat') 
                self.Button9.configure(cursor='hand2')
                self.Button9.configure(command=botao9)

                self.Label9 = tk.Label(self.Frame9)
                self.Label9.place(relx=0.0, rely=0.721, height=51, width=144)
                self.Label9.configure(activebackground="#f9f9f9")
                self.Label9.configure(activeforeground="black")
                self.Label9.configure(background="#d9d9d9")
                self.Label9.configure(disabledforeground="#a3a3a3")
                self.Label9.configure(font="-family {Segoe UI} -size 18 -weight bold")
                self.Label9.configure(foreground="#000000")
                self.Label9.configure(highlightbackground="#d9d9d9")
                self.Label9.configure(highlightcolor="black")
                self.Label9.configure(justify='right')
                self.Label9.configure(text='Kindle 10º')

                self.desc9 = tk.Label(self.Frame9)
                self.desc9.place(relx=0.04, rely=0.885, height=21, width=124)
                self.desc9.configure(activebackground="#f9f9f9")
                self.desc9.configure(activeforeground="black")
                self.desc9.configure(background="#d9d9d9")
                self.desc9.configure(disabledforeground="#a3a3a3")
                self.desc9.configure(foreground="#0995FE")
                self.desc9.configure(text='R$379,05')
                self.desc9.configure(anchor='w', font=font8)

                self.imagem9 = tk.Label(self.Frame9)
                self.imagem9.place(relx=0.039, rely=0.066, height=191, width=238)
                self.imagem9.configure(background="#d9d9d9")
                self.imagem9.configure(disabledforeground="#a3a3a3")
                img9 = tk.PhotoImage(file='C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\kindle.png')
                self.imagem9.configure(image=img9)
        
                '''Décimo frame, botão, imagem, Nome do produto e descrição''' # 10° FRAME
                self.Frame10 = tk.Frame(self.top)
                self.Frame10.place(relx=0.805, rely=0.55, relheight=0.409, relwidth=0.186)
                self.Frame10.configure(relief='flat')
                self.Frame10.configure(borderwidth="2")
                self.Frame10.configure(background="#d9d9d9")
                self.Frame10.configure(highlightbackground="#d9d9d9")
                self.Frame10.configure(highlightcolor="black")

                self.Frame1_10 = tk.Frame(self.Frame10)
                self.Frame1_10.place(relx=3.209, rely=1.318, relheight=1.0, relwidth=1.0)

                self.Frame1_10.configure(relief='flat')
                self.Frame1_10.configure(borderwidth="2")
                self.Frame1_10.configure(background="#d9d9d9")
                self.Frame1_10.configure(highlightbackground="#d9d9d9")
                self.Frame1_10.configure(highlightcolor="black")

                self.Button10 = tk.Button(self.Frame10)
                self.Button10.place(relx=0.787, rely=0.82, height=44, width=46)
                self.Button10.configure(activebackground="#ececec")
                self.Button10.configure(activeforeground="#000000")
                self.Button10.configure(background="#d9d9d9")
                self.Button10.configure(disabledforeground="#a3a3a3")
                self.Button10.configure(foreground="#000000")
                self.Button10.configure(highlightbackground="#d9d9d9")
                self.Button10.configure(highlightcolor="black")
                self.Button10.configure(image=bt1)
                self.Button10.configure(relief='flat') 
                self.Button10.configure(cursor='hand2')
                self.Button10.configure(command=botao10)

                self.Label10 = tk.Label(self.Frame10)
                self.Label10.place(relx=0.0, rely=0.721, height=51, width=190)
                self.Label10.configure(activebackground="#f9f9f9")
                self.Label10.configure(activeforeground="black")
                self.Label10.configure(background="#d9d9d9")
                self.Label10.configure(disabledforeground="#a3a3a3")
                self.Label10.configure(font="-family {Segoe UI} -size 15 -weight bold")
                self.Label10.configure(foreground="#000000")
                self.Label10.configure(highlightbackground="#d9d9d9")
                self.Label10.configure(highlightcolor="black")
                self.Label10.configure(justify='right')
                self.Label10.configure(text='Geladeira Frost Free')

                self.desc10 = tk.Label(self.Frame10)
                self.desc10.place(relx=0.02, rely=0.885, height=21, width=124)
                self.desc10.configure(activebackground="#f9f9f9")
                self.desc10.configure(activeforeground="black")
                self.desc10.configure(background="#d9d9d9")
                self.desc10.configure(foreground="#0995FE")
                self.desc10.configure(text='R$2980,00')
                self.desc10.configure(anchor='w', font=font8)

                #IMAGEM DO PRODUTO
                self.imagem10 = tk.Label(self.Frame10)
                self.imagem10.place(relx=0.079, rely=0.066, height=201, width=204)
                self.imagem10.configure(background="#d9d9d9")
                self.imagem10.configure(disabledforeground="#a3a3a3")
                img10 = tk.PhotoImage(file='C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\geladeira.png')
                self.imagem10.configure(image=img10)

                self.top.mainloop()

                

        '''Janela 3'''

        def janela3(self):
                '''This class configures and populates the toplevel window.
                top is the toplevel containing window.'''
                _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
                _fgcolor = '#000000'  # X11 color: 'black'
                _compcolor = '#d9d9d9' # X11 color: 'gray85'
                _ana1color = '#d9d9d9' # X11 color: 'gray85'
                _ana2color = '#ececec' # Closest X11 color: 'gray92'
                font10 = "-family {Segoe UI} -size 24 -weight bold"
                font13 = "-family {Segoe UI} -size 20 -weight bold"
                font14 = "-family {Segoe UI} -size 22 -weight bold"
                font16 = "-family {Segoe UI} -size 12 -weight bold"
                font9 = "-family {Segoe UI} -size 23 -weight bold"

                self.top.destroy() #Destruir janela anterior
                self.top3 = tk.Tk()
                self.top3.attributes('-fullscreen', True)
                self.top3.resizable(0, 0)
                self.top3.title("Colinas Magazine")
                self.top3.configure(background="#ffffff")

                self.frametop3 = tk.Frame(self.top3)
                self.frametop3.place(relx=-0.007, rely=-0.013, relheight=0.10 , relwidth=1.071)
                self.frametop3.configure(relief='flat')
                self.frametop3.configure(borderwidth="2")
                self.frametop3.configure(background="#0995FE")

                self.imgltop3 = tk.Label(self.frametop3)
                self.imgltop3.place(relx=0.007, rely=0.132, height=71, width=95)
                self.imgltop3.configure(background="#d9d9d9")
                self.imgltop3.configure(disabledforeground="#a3a3a3")
                self.imgltop3.configure(foreground="#000000")
                img = tk.PhotoImage(file='C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\logo.png')
                self.imgltop3.configure(image=img)
        

                self.nomeloja3 = tk.Label(self.frametop3)
                self.nomeloja3.place(relx=0.075, rely=0.263, height=51, width=276)
                self.nomeloja3.configure(activebackground="#f9f9f9")
                self.nomeloja3.configure(activeforeground="black")
                self.nomeloja3.configure(anchor='w')
                self.nomeloja3.configure(background="#0995FE")
                self.nomeloja3.configure(disabledforeground="#a3a3a3")
                self.nomeloja3.configure(font=font10)
                self.nomeloja3.configure(foreground="#ffffff")
                self.nomeloja3.configure(highlightbackground="#d9d9d9")
                self.nomeloja3.configure(highlightcolor="black")
                self.nomeloja3.configure(text='''Colinas Magazine''')
                
                '''Entry 1(que recebe o nome do cliente)'''     
                self.Entry1 = tk.Entry(self.top3)
                self.Entry1.place(relx=0.029, rely=0.201,height=50, relwidth=0.562)
                self.Entry1.configure(background="#c0c0c0")
                self.Entry1.configure(disabledforeground="#a3a3a3")
                self.Entry1.configure(font=font16)
                self.Entry1.configure(foreground="#000000")
                self.Entry1.configure(insertbackground="black")
                self.Entry1.configure(relief="flat")

                '''Entry 2(que recebe a data de nascimento do cliente)''' 
                self.entry_nas = tk.Entry(self.top3)
                self.entry_nas.place(relx=0.029, rely=0.335,height=50, relwidth=0.562)
                self.entry_nas.configure(background="#c0c0c0")
                self.entry_nas.configure(disabledforeground="#a3a3a3")
                self.entry_nas.configure(font=font16)
                self.entry_nas.configure(foreground="#000000")
                self.entry_nas.configure(highlightbackground="#d9d9d9")
                self.entry_nas.configure(highlightcolor="black")
                self.entry_nas.configure(insertbackground="black")
                self.entry_nas.configure(relief="flat")
                self.entry_nas.configure(selectbackground="#c4c4c4")
                self.entry_nas.configure(selectforeground="black")

                '''Entry 3(que recebe o CPF do cliente)''' 
                self.entry_cpf = tk.Entry(self.top3)
                self.entry_cpf.place(relx=0.596, rely=0.335,height=50, relwidth=0.334)
                self.entry_cpf.configure(background="#c0c0c0")
                self.entry_cpf.configure(disabledforeground="#a3a3a3")
                self.entry_cpf.configure(font=font16)
                self.entry_cpf.configure(foreground="#000000")
                self.entry_cpf.configure(highlightbackground="#d9d9d9")
                self.entry_cpf.configure(highlightcolor="black")
                self.entry_cpf.configure(insertbackground="black")
                self.entry_cpf.configure(relief="flat")
                self.entry_cpf.configure(selectbackground="#c4c4c4")
                self.entry_cpf.configure(selectforeground="black")

                '''Entry 4(que recebe o endereço do cliente)''' 
                self.entry_en = tk.Entry(self.top3)
                self.entry_en.place(relx=0.029, rely=0.469,height=50, relwidth=0.562)
                self.entry_en.configure(background="#c0c0c0")
                self.entry_en.configure(disabledforeground="#a3a3a3")
                self.entry_en.configure(font=font16)
                self.entry_en.configure(foreground="#000000")
                self.entry_en.configure(highlightbackground="#d9d9d9")
                self.entry_en.configure(highlightcolor="black")
                self.entry_en.configure(insertbackground="black")
                self.entry_en.configure(relief="flat")
                self.entry_en.configure(selectbackground="#c4c4c4")
                self.entry_en.configure(selectforeground="black")

                '''Entry 5(que recebe o número da casa do cliente)''' 
                self.entry_ndc = tk.Entry(self.top3)
                self.entry_ndc.place(relx=0.596, rely=0.469,height=50, relwidth=0.334)
                self.entry_ndc.configure(background="#c0c0c0")
                self.entry_ndc.configure(disabledforeground="#a3a3a3")
                self.entry_ndc.configure(font=font16)
                self.entry_ndc.configure(foreground="#000000")
                self.entry_ndc.configure(highlightbackground="#d9d9d9")
                self.entry_ndc.configure(highlightcolor="black")
                self.entry_ndc.configure(insertbackground="black")
                self.entry_ndc.configure(relief="flat")
                self.entry_ndc.configure(selectbackground="#c4c4c4")
                self.entry_ndc.configure(selectforeground="black")

                self.name = tk.Label(self.top3)
                self.name.place(relx=0.029, rely=0.134, height=41, width=255)
                self.name.configure(anchor='w')
                self.name.configure(background="#ffffff")
                self.name.configure(disabledforeground="#a3a3a3")
                self.name.configure(font=font9)
                self.name.configure(foreground="#0995FE")
                self.name.configure(justify='right')
                self.name.configure(text='''Nome completo:''')

                self.birthdate = tk.Label(self.top3)
                self.birthdate.place(relx=0.029, rely=0.268, height=41, width=308)
                self.birthdate.configure(activebackground="#f9f9f9")
                self.birthdate.configure(activeforeground="black")
                self.birthdate.configure(anchor='w')
                self.birthdate.configure(background="#ffffff")
                self.birthdate.configure(disabledforeground="#a3a3a3")
                self.birthdate.configure(font="-family {Segoe UI} -size 23 -weight bold")
                self.birthdate.configure(foreground="#0995FE")
                self.birthdate.configure(highlightbackground="#d9d9d9")
                self.birthdate.configure(highlightcolor="black")
                self.birthdate.configure(text='''Data de nascimento:''')

                self.address = tk.Label(self.top3)
                self.address.place(relx=0.029, rely=0.402, height=41, width=256)
                self.address.configure(activebackground="#f9f9f9")
                self.address.configure(activeforeground="black")
                self.address.configure(anchor='w')
                self.address.configure(background="#ffffff")
                self.address.configure(disabledforeground="#a3a3a3")
                self.address.configure(font="-family {Segoe UI} -size 23 -weight bold")
                self.address.configure(foreground="#0995FE")
                self.address.configure(highlightbackground="#d9d9d9")
                self.address.configure(highlightcolor="black")
                self.address.configure(text='''Endereço:''')

                self.numberhouse = tk.Label(self.top3)
                self.numberhouse.place(relx=0.596, rely=0.402, height=41, width=255)
                self.numberhouse.configure(activebackground="#f9f9f9")
                self.numberhouse.configure(activeforeground="black")
                self.numberhouse.configure(anchor='w')
                self.numberhouse.configure(background="#ffffff")
                self.numberhouse.configure(disabledforeground="#a3a3a3")
                self.numberhouse.configure(font="-family {Segoe UI} -size 23 -weight bold")
                self.numberhouse.configure(foreground="#0995FE")
                self.numberhouse.configure(highlightbackground="#d9d9d9")
                self.numberhouse.configure(highlightcolor="black")
                self.numberhouse.configure(text='''N° da casa:''')

                self.cpf = tk.Label(self.top3)
                self.cpf.place(relx=0.596, rely=0.282, height=41, width=255)
                self.cpf.configure(activebackground="#f9f9f9")
                self.cpf.configure(activeforeground="black")
                self.cpf.configure(anchor='w')
                self.cpf.configure(background="#ffffff")
                self.cpf.configure(disabledforeground="#a3a3a3")
                self.cpf.configure(font="-family {Segoe UI} -size 23 -weight bold")
                self.cpf.configure(foreground="#0995FE")
                self.cpf.configure(highlightbackground="#d9d9d9")
                self.cpf.configure(highlightcolor="black")
                self.cpf.configure(text='''CPF:''')

                self.purchase_value = tk.Label(self.top3)
                self.purchase_value.place(relx=0.647, rely=0.59, height=41, width=364)
                self.purchase_value.configure(activebackground="#f9f9f9")
                self.purchase_value.configure(activeforeground="black")
                self.purchase_value.configure(anchor='w')
                self.purchase_value.configure(background="#ffffff")
                self.purchase_value.configure(disabledforeground="#a3a3a3")
                self.purchase_value.configure(font="-family {Segoe UI} -size 23 -weight bold")
                self.purchase_value.configure(foreground="#000000")
                self.purchase_value.configure(highlightbackground="#d9d9d9")
                self.purchase_value.configure(highlightcolor="black")
                self.purchase_value.configure(text='''Valor da compra em R$:''')

                self.valuep = tk.Label(self.top3)
                self.valuep.place(relx=0.662, rely=0.657, height=71, width=316)
                self.valuep.configure(background="#ffffff")
                self.valuep.configure(disabledforeground="#a3a3a3")
                self.valuep.configure(font=font10)
                self.valuep.configure(foreground="#0995FE")
                self.valuep.configure(text='00.00')

                self.Btnfinalcompra = tk.Button(self.top3)
                self.Btnfinalcompra.place(relx=0.404, rely=0.831, height=84, width=337)
                self.Btnfinalcompra.configure(activebackground="#ececec")
                self.Btnfinalcompra.configure(activeforeground="#000000")
                self.Btnfinalcompra.configure(background="#0995FE")
                self.Btnfinalcompra.configure(disabledforeground="#a3a3a3")
                self.Btnfinalcompra.configure(font=font14)
                self.Btnfinalcompra.configure(foreground="#ffffff")
                self.Btnfinalcompra.configure(highlightbackground="#d9d9d9")
                self.Btnfinalcompra.configure(highlightcolor="black")
                self.Btnfinalcompra.configure(pady="0")
                self.Btnfinalcompra.configure(relief="flat")
                self.Btnfinalcompra.configure(text='''Finalizar compra''')
                self.Btnfinalcompra.configure(command=lambda:[self.pro(), self.janela4()])
                self.Btnfinalcompra.configure(cursor='hand2')

                self.Frame1 = tk.Frame(self.top3)
                self.Frame1.place(relx=0.029, rely=0.576, relheight=0.343, relwidth=0.365)
                self.Frame1.configure(relief='flat')
                self.Frame1.configure(borderwidth="2")
                self.Frame1.configure(background="#ffffff")
                
                self.rbtn = StringVar()
                '''Radiobuttonmoney(retorna que a compra será em dinheiro)''' 
                self.Radiobuttonmoney = tk.Radiobutton(self.Frame1)
                self.Radiobuttonmoney.place(relx=0.06, rely=0.313, relheight=0.176, relwidth=0.579)
                self.Radiobuttonmoney.configure(activebackground="#ececec")
                self.Radiobuttonmoney.configure(activeforeground="#000000")
                self.Radiobuttonmoney.configure(anchor='w')
                self.Radiobuttonmoney.configure(background="#ffffff")
                self.Radiobuttonmoney.configure(disabledforeground="#a3a3a3")
                self.Radiobuttonmoney.configure(font="-family {Segoe UI} -size 16 -weight bold")
                self.Radiobuttonmoney.configure(foreground="#0995FE")
                self.Radiobuttonmoney.configure(highlightbackground="#d9d9d9")
                self.Radiobuttonmoney.configure(highlightcolor="black")
                self.Radiobuttonmoney.configure(justify='left')
                self.Radiobuttonmoney.configure(text='Dinheiro')
                self.Radiobuttonmoney.configure(value='dinheiro')
                self.Radiobuttonmoney.configure(variable=self.rbtn)

                self.payment = tk.Label(self.Frame1)
                self.payment.place(relx=0.02, rely=0.039, height=41, width=365)
                self.payment.configure(activebackground="#f9f9f9")
                self.payment.configure(activeforeground="black")
                self.payment.configure(anchor='w')
                self.payment.configure(background="#ffffff")
                self.payment.configure(disabledforeground="#a3a3a3")
                self.payment.configure(font="-family {Segoe UI} -size 23 -weight bold")
                self.payment.configure(foreground="#000000")
                self.payment.configure(highlightbackground="#d9d9d9")
                self.payment.configure(highlightcolor="black")
                self.payment.configure(text='''Forma de pagamento:''')

                '''Radiobuttoncard(retorna que a compra será no cartão)''' 
                self.Radiobuttoncard = tk.Radiobutton(self.Frame1)
                self.Radiobuttoncard.place(relx=0.06, rely=0.508, relheight=0.176, relwidth=0.579)
                self.Radiobuttoncard.configure(activebackground="#ececec")
                self.Radiobuttoncard.configure(activeforeground="#000000")
                self.Radiobuttoncard.configure(anchor='w')
                self.Radiobuttoncard.configure(background="#ffffff")
                self.Radiobuttoncard.configure(disabledforeground="#a3a3a3")
                self.Radiobuttoncard.configure(font="-family {Segoe UI} -size 16 -weight bold")
                self.Radiobuttoncard.configure(foreground="#0995FE")
                self.Radiobuttoncard.configure(highlightbackground="#d9d9d9")
                self.Radiobuttoncard.configure(highlightcolor="black")
                self.Radiobuttoncard.configure(justify='left')
                self.Radiobuttoncard.configure(text='Cartão')
                self.Radiobuttoncard.configure(value='cartao')
                self.Radiobuttoncard.configure(variable=self.rbtn)

                '''Contador que irá somar o valor da compra e substituir 
                a label de preço pelo valor!
                Variável c < essa é a varável que armazena o valor da compra
                '''
                c = sum(preco) 
                self.valuep['text'] = c

                self.top3.mainloop()
                
                
        def pro(self):
                v_rbtn = self.rbtn.get() #Variável que vai receber a forma de pagamento
                n = self.Entry1.get() #Variável que recebe o nome
                cpf = self.entry_cpf.get() #Variável que recebe o cpf
                ndc = self.entry_ndc.get() #Variável que recebe o número da casa
                en = self.entry_en.get() #Variável que recebe o endereço
                na = self.entry_nas.get() #Variável qie recebe a data de nascimento
                file = open("files_.txt", "w")
                for i in range(len(carrinho)):
                        file.write(carrinho[i]+"\n")
                for j in range(len(preco)):
                        file.write(str(preco[j])+"\n")
                file.write(v_rbtn + "\n")
                file.write(n + "\n")
                file.write(cpf + "\n")
                file.write(ndc + "\n")
                file.write(en + "\n")
                file.write(na + "\n")
                file.close()
                
                # print(n) #Nome 
                # print(cpf) #Cpf
                # print(ndc) #CPF
                # print(en) #nDA CASA
                # print(na) #idade
                # print(v_rbtn) #forma de pagamento


        '''Janela 4(apenas um pop up informando que a compra foi efetivada)'''
        def janela4(self):
                self.top3.destroy() #Destruir janela anterior
                self.top4 = tk.Tk()
                self.top4.geometry("400x250+300+300")
                self.top4.resizable(0, 0)
                self.top4.title('Colinas Magazine')

                self.labagrad = tk.Label(self.top4)
                self.labagrad.place(x=0, y=0, width=400, height=250)
                self.labagrad.configure(
                        background='#0995FE',
                        foreground='#ffffff',
                        justify='center',
                        font="-family {Segoe UI} -size 16 -weight bold",
                        text='Sua compra foi efetivada. \n Obrigado por escolher nossos serviços!',
                        anchor='s'
                )
                self.labf = tk.Label(self.top4)
                self.labf.place(relx= 0.25, rely=0.0, width=200, height=185)
                imloja = tk.PhotoImage(file='C:\\Users\\seven\\Desktop\\python\\app lpg\\img\\loj.png')
                self.labf.configure(image=imloja)
                
                self.top4.mainloop()


'''Funções(eventos)''' 
carrinho = []
preco =[] #Usar a lista preço para somar os valores que forem adicionados, lembrando que o tipo dos valores é float.
#Usar o for para somar os valores exemplo > https://www.alura.com.br/artigos/listas-no-python 

#Produto 1
def botao1():
        item1 = 'Smart TV'
        item1preco = 2700.00
        carrinho.append(item1)
        preco.append(item1preco)
        print('Smart tv')

#Produto 2
def botao2():
        item2 = 'Lava e Seca'
        item2preco = 3699.00
        carrinho.append(item2)
        preco.append(item2preco)
        print('Lava e Seca')

#Produto3
def botao3():
        item3 = 'Iphone 12'
        item3preco = 7029.00
        carrinho.append(item3)
        preco.append(item3preco)
        print('Iphone 12')

#Produto4
def botao4():
        item4 = 'Fone Bluetooth'
        item4preco = 197.91
        carrinho.append(item4)
        preco.append(item4preco)
        print('Fone Bluetooth')

#Produto5
def botao5():
        item5 = 'Cooktop'
        item5preco = 581.83
        carrinho.append(item5)
        preco.append(item5preco)
        print('Cooktop')

#Produto6
def botao6():
        item6 = 'Cadeira Giratória'
        item6preco = 759.98
        carrinho.append(item6)
        preco.append(item6preco)
        print('Cadeira')

#Produto7
def botao7():
        item7 = 'Impressora EPSON'
        item7preco = 949.85
        carrinho.append(item7)
        preco.append(item7preco)
        print('Impressora')

#Produto8
def botao8():
        item8 = 'Notebook 8gb'
        item8preco = 5034.00
        carrinho.append(item8)
        preco.append(item8preco)
        print('Notebook')

#Produto9
def botao9():
        item9 = 'Kindle 10º'
        item9preco = 379.05
        carrinho.append(item9)
        preco.append(item9preco)
        print('Kindle')

#Produto10
def botao10():
        item10 = 'Geladeira Frost Free'
        item10preco = 2980.00
        carrinho.append(item10)
        preco.append(item10preco)
        print('Geladeira')


#Chamando a classe

Toplevel1()





