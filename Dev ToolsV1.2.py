"""
   MENU
   TOOLS
   TKINTER
"""
from tkinter import *
from tkinter import ttk
import sys
from time import sleep

versao = '1.2'
emais = []
email = ''
pw = ''
class Menu_App:
    #initial function
    def __init__(self, window_m):
        #window
        window_m.title('TOOLS BY DEUKAUS')
        window_m['bg'] = 'red'
 
        #labels
        self.title1 = Label(window_m, bg = 'red', font='bold 20 bold', fg = 'black', text = 'MENU\nTOOLS')
        self.lb_versao = Label(window_m, bg = 'red', font='bold 9 bold', fg = 'black', text = 'Versão {}'.format(versao))
 
        #buttons
        self.btn_credits = Button(window_m, bg = '#E0E0E0', text = 'Creditos', font = 'bold 20 bold', command=self.go_to_creditos, width = 10, height = 1)
        self.btn_bot_email = Button(window_m, bg = '#E0E0E0', text = 'Bot Emails', font = 'bold 20 bold', command=self.go_to_bot_email, width = 10, height = 1)
        self.btn_rdsc = Button(window_m, bg = '#E0E0E0', text = 'Redes\nSociais', font = 'bold 20 bold', command = self.go_to_redessociais, width = 10, height = 1)
        self.btn_exit = Button(window_m, bg = '#E0E0E0', text = 'Sair', font = 'bold 20 bold', command=self.go_to_exit, width = 10, height = 1)
       
        #grid
        self.title1.grid(column='0', row='0')
        self.btn_credits.grid(column='0', row='1')
        self.btn_bot_email.grid(column='0', row='2', pady = 3)
        self.btn_rdsc.grid(column='0', row='3')
        self.btn_exit.grid(column='0', row='4', pady = 3)
        self.lb_versao.grid(column='0', row='5')
 
    #commands
    def go_to_creditos(self):
        global menu_creditos_root
        menu_creditos_root = Tk()
        Menu_Creditos(menu_creditos_root)
        menu_creditos_root.mainloop()
 
    def go_to_bot_email(self):
        global loguin_email_root
        loguin_email_root = Tk()
        logar_bot_email(loguin_email_root)
        loguin_email_root.mainloop()

    def go_to_exit(self):
        try:
            exit()
        except:
            menu_root.destroy()

    def go_to_redessociais(self):
        pass
 
class Menu_bot_email:
    def __init__(self, window_mb):
        #window
        window_mb.title('BOT EMAIL')
        window_mb['bg'] = 'white'

        #menu
        self.itens_menu = Menu(window_mb)
        self.menu_item_file = Menu(window_mb, tearoff=0)
        self.menu_item_personalizar = Menu(window_mb)
        self.menu_item_help = Menu(window_mb, tearoff=0)
        self.submenu_redessociais = Menu(window_mb, tearoff=0)

        #menu itens
        self.menu_item_file.add_command(label = 'Save', command = self.save)
        self.menu_item_help.add_command(label = 'tutorial', command = self.tutorial)
        self.menu_item_help.add_command(label = 'creditos', command = self.creditos)
        self.menu_item_help.add_cascade(label = 'redes sociais', menu=self.submenu_redessociais)
        self.submenu_redessociais.add_command(label = 'WebSite', command = self.website)
        self.submenu_redessociais.add_command(label = 'Facebook', command = self.facebook)
        self.submenu_redessociais.add_command(label = 'YouTube', command = self.youtube)
        self.itens_menu.add_cascade(label = 'File', menu = self.menu_item_file)
        self.itens_menu.add_cascade(label = 'Personalizar', command = self.personalizar)
        self.itens_menu.add_cascade(label = 'options', command = self.abrir_opcoes)
        self.itens_menu.add_cascade(label = 'Help', menu = self.menu_item_help)

        #buttons
        self.open_add_email = Button(window_mb, text = 'Adicionar Email', font = 'bold 20 bold', bg = '#E0E0E0', command = self.abrir_add_email)

        #Adiciona menu ao window_mb
        window_mb.config(menu = self.itens_menu)

        #grid
        self.open_add_email.grid(column='0', row='1')

    def abrir_opcoes(self):
        pass

    def tutorial(self):
        print('teste')

    def save(self):
        pass

    def creditos(self):
        pass

    def website(self):
        pass

    def facebook(self):
        pass

    def youtube(self):
        pass

    def personalizar(self):
        pass
        
    def abrir_add_email(self):
        pass
         
class Menu_Creditos:
    def __init__(self, window_mc):
        #window
        window_mc.title('CREDITOS')
        window_mc['bg'] = 'blue'
 
        #Labels
         
        #grid

class logar_bot_email:
    def __init__(self, window_lbe):
        window_lbe.title('Loguin')
        window_lbe['bg'] = 'blue'

        #variables
        self.statuslog = ''

        self.itens_menu_logar = Menu(window_lbe)
        self.itens_menu_logar.add_cascade(label = 'Tutorial', command = self.tutorial)
        window_lbe.config(menu = self.itens_menu_logar)
        #labels
        self.label1 = Label(window_lbe,text = 'Email : ', bg = 'blue', fg = 'red', font = 'bold')
        self.label2 = Label(window_lbe, text = 'Senha : ', bg = 'blue', fg = 'red', font = 'bold')
        self.label3 = Label(window_lbe, text =  self.statuslog, bg = 'blue', fg = 'red', font = 'bold')

        #buttons
        self.btn_logar = Button(window_lbe, text = 'Logar', bg = '#E0E0E0', font = 'bold 10 bold', width = 15, command = self.loguinn)

        #entry
        self.ent_email = Entry(window_lbe, justify = 'left')
        self.ent_passw = Entry(window_lbe, justify = 'left', show ='*')

        #grid
        self.label1.grid(column='0', row='1', pady='5')
        self.ent_email.grid(column='1', row='1', padx='5', pady='5')
        self.label2.grid(column='0', row='2', pady='5')
        self.ent_passw.grid(column='1', row='2', padx='5', pady='5')
        self.btn_logar.grid(column='0',columnspan='2', row='3', pady='5')
        
        
    def tutorial(self):
        pass

    def loguinn(self):
        global email_user
        email_user = self.ent_email.get()
        global passw_user
        passw_user = self.ent_passw.get()
        if '@' in email_user:
            if passw_user == '':
                self.statuslog = 'A senha não pode estar vazia!'
                self.label3['text'] = self.statuslog
                self.label3.grid(column='0', columnspan='2', row='5', pady='5')
            else:
                sleep(3)
                loguin_email_root.destroy()
                global menu_bot_email_root
                menu_bot_email_root = Tk()
                Menu_bot_email(menu_bot_email_root)
                loguin_email_root.mainloop()
                menu_bot_email_root.mainloop()
        elif email_user != '':
            self.statuslog = 'Por favor, insira um email valido!'
            self.label3['text'] = self.statuslog
            self.label3.grid(column='0', columnspan='2', row='5', pady='5')

        elif email_user == '' and passw_user == '':
            self.statuslog = 'Os campos não podem estar vazios!'
            self.label3['text'] = self.statuslog
            self.label3.grid(column='0',columnspan='2',row='5', pady='5')

        elif email_user == '':
            self.statuslog = 'O email não pode estar vazio!'
            self.label3['text'] = self.statuslog
            self.label3.grid(column='0', columnspan='2', row='5', pady='5')            


       
 
 
menu_root = Tk()
Menu_App(menu_root)
menu_root.mainloop()
