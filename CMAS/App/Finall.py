from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
import glink



	



username_input = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "account-box"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:600
"""

Toolbar = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "                       Citizen Monitoring and Aiding Application"

    MDLabel:
        halign: "center"
'''




class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"  
        self.theme_cls.primary_palette = "Green"
        screen = Screen()

        self.username = Builder.load_string(username_input)
        button = MDRectangleFlatButton(text='Show Travel Histroy',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.45},
                                       on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)
        self.Toolbar=Builder.load_string(Toolbar)
        screen.add_widget(self.Toolbar)
        return screen
        
      
    def show_data(self, obj):
        if self.username.text is not "":
            user_error =self.username.text
            print(user_error)
            gl = glink.collect(user_error)
        else:
        	 user_error = "Please enter a username"

        self.dialog = MDDialog(title='Travel History',
                               text=gl, size_hint=(0.8, 1),
                               						     buttons=[MDRectangleFlatButton(text='Close',     on_release=self.close_dialog)]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()   
        
         


   


DemoApp().run()