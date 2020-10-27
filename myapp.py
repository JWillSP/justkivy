from kivy.app import App
from kivy.uix.button import Button
from kivy.lang.builder import Builder


kv_string = '''
BoxLayout:
    orientation: 'vertical'
    ActionBar:
        ActionView:
            use_separator: True
            ActionPrevious:
                title: 'Action Bar'
                with_previous: False
            ActionOverflow:
            ActionButton:
                text: 'Btn'
                on_release: app.to_add(FL) if not app.mybtn else None
    FloatLayout
        id: FL
        on_touch_up: app.to_remove(self) if app.mybtn else None

<Mbtn>:
    text: "oi"
    size_hint: 0.2, 0.2
    pos_hint: {'center_x': 0.6, 'top': 0.6}
    on_press: 
        app.to_remove(self.parent)
        app.mybtn = None
'''
class Mbtn(Button):
    pass 


class Mapp(App):
    def build(self):
        self.mybtn = None
        return Builder.load_string(kv_string)

    def to_add(self, parent):
        self.mybtn = Mbtn()
        parent.add_widget(self.mybtn)

    def to_remove(self, parent):
        parent.remove_widget(self.mybtn)
        self.mybtn = None

Mapp().run()