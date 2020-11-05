from kivymd.app import MDApp
from kivy.core.audio import SoundLoader


ERROU = SoundLoader.load('errou_faustao.mp3')
PARABENS = SoundLoader.load('parabens.mp3')

class MainApp(MDApp):

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