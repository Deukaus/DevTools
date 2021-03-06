"""
   MENU
   TOOLS
   TKINTER
"""
 
from tkinter import *
from tkinter import ttk
import sys
versao = '1.1'

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
        self.btn_exit = Button(window_m, bg = '#E0E0E0', text = 'Sair', font = 'bold 20 bold', command=self.go_to_exit, width = 10, height = 1)
       
        #grid
        self.title1.grid(column='0', row='0')
        self.btn_credits.grid(column='0', row='1')
        self.btn_bot_email.grid(column='0', row='2', pady = 3)
        self.btn_exit.grid(column='0', row='3')
        self.lb_versao.grid(column='0', row='4')
 
    #commands
    def go_to_creditos(self):
        global menu_creditos_root
        menu_creditos_root = Tk()
        Menu_Creditos(menu_creditos_root)
        menu_creditos_root.mainloop()
 
    def go_to_bot_email(self):
        global menu_bot_email_root
        menu_bot_email_root = Tk()
        Menu_bot_email(menu_bot_email_root)
        menu_bot_email_root.mainloop()
       
 
    def go_to_exit(self):
        try:
            exit()
        except:
            menu_root.destroy()
 
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
        self.itens_menu.add_cascade(label = 'Help', menu = self.menu_item_help)

        #Adiciona menu ao window_mb
        window_mb.config(menu = self.itens_menu)


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
        

         
class Menu_Creditos:
    def __init__(self, window_mc):
        #window
        window_mc.title('CREDITOS')
        window_mc['bg'] = 'blue'
 
        #Labels
         
        #grid
 

       
 
 
menu_root = Tk()
Menu_App(menu_root)
menu_root.mainloop()
