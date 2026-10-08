from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"

        screen = MDScreen()

        layout = MDBoxLayout(
            orientation="vertical",
            padding=40,
            spacing=20,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        # Title
        title = MDLabel(
            text="Hello World!",
            halign="center",
            font_style="H3",
            size_hint_y=None,
            height=100,
        )

        # Text input
        self.name_input = MDTextField(
            hint_text="Enter your name",
            size_hint_y=None,
            height=60,
        )

        # Button
        btn = MDRaisedButton(
            text="Click Me!",
            pos_hint={"center_x": 0.5},
            size_hint=(0.5, None),
            height=60,
        )
        btn.bind(on_release=self.on_click)

        # Result label
        self.result = MDLabel(
            text="",
            halign="center",
            font_style="H5",
            size_hint_y=None,
            height=80,
        )

        layout.add_widget(title)
        layout.add_widget(self.name_input)
        layout.add_widget(btn)
        layout.add_widget(self.result)

        screen.add_widget(layout)
        return screen

    def on_click(self, instance):
        name = self.name_input.text or "Guest"
        self.result.text = f"Hello {name}! Welcome!"


if __name__ == "__main__":
        MyApp().run()

