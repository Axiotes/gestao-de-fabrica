from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import conexaoBD

database = conexaoBD.BancoDedados()
database.conectar()

Window.clearcolor = (30/100, 52/100, 86/100, 1)

class GerenciarTelas(ScreenManager):
    pass

class TelaInicial(Screen):
    pass

class TelaCliente(Screen):
    def entrar(self):
        #gmail = self.ids.gmailCliente.text
        #senha = self.ids.senhaCliente.text

        print('Teste entrar')
            




class TelaFuncionario(Screen):
    def entrar(self):
        print('Teste entrar')

class TelaCadastroCliente(Screen):
    def confirmar(self):
        nomeCompleto = self.ids.nomeCliente.text

        cpf = self.ids.cpfCliente.text
        nomeCompleto = nomeCompleto.upper()

        gmail = self.ids.gmailCliente.text
        gmail = gmail.lower()

        senha = self.ids.senhaCliente.text
        
        database.addCliente(nomeCompleto, cpf, gmail, senha)

class TelaCadastroConfirmado(Screen):
    pass

class GestaoDeFabrica(App):
    def build(self):
        return Builder.load_file("telaGestao.kv")

GestaoDeFabrica().run()