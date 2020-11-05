KV='''
ScreenManager:
    Screen:
        name: "login"
        MDCard:
            orientation: "vertical"
            padding: "8dp"
            size_hint: None, None
            size: root.height/3, root.height/2
            pos_hint: {"center_x": .5, "center_y": .5}
            MDLabel:
                text: "Login"
                theme_text_color: "Secondary"
                size_hint_y: None
                height: self.texture_size[1]
            MDSeparator:
                height: "1dp"
            MDLabel:
                text: ""
            MDTextField:
                id: user
                hint_text: "Nome do Usuário"
            MDLabel:
                text: ""
            MDTextField:
                id: pwd
                hint_text: "Senha"
                password: True
            MDLabel:
                id: display
                text: ""
                halign: "center"
                theme_text_color: "Error"
            MDRaisedButton:
                text: "enviar"
                on_release: app.check_crendentials(user.text, pwd.text, display)
                pos_hint: {"center_x": .5}
    Screen:
        name: "logado"
        MDLabel:
            text: "PARABÉNS"
            halign: "center"
        MDRaisedButton:
            text: "voltar"
            on_release: root.current = 'login'
            pos_hint: {"center_x": .5, "center_y": .4}

'''

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.audio import SoundLoader

print("1")
ERROU = SoundLoader.load(r'./audios/errou_faustao.mp3')
PARABENS = SoundLoader.load('./audios/parabens.mp3')
print("2")
class MainApp(MDApp):
    
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.user = "Ronadab"
        self.password = "freefire"

    def check_crendentials(self, user, password, label):
        if (
            (self.user == user) and (self.password == password)
        ):
            self.play_sucess()
            self.root.current = "logado"
            label.text = ""
        else:
            self.play_error()
            label.text = "Errrouuuuu"

    def play_error(self):
        ERROU.play()
    
    def play_sucess(self):
        PARABENS.play()


if __name__ == "__main__":
    MainApp().run()