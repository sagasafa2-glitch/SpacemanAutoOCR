
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock


class SpacemanMonitor(App):

    def build(self):
        self.title = "Spaceman Auto OCR Monitor"

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        layout.add_widget(Label(
            text="[b]SPACEMAN AUTO OCR MONITOR[/b]",
            markup=True,
            font_size="22sp"
        ))

        self.status = Label(
            text="Status: Menunggu data",
            font_size="16sp"
        )
        layout.add_widget(self.status)

        self.multiplier = TextInput(
            hint_text="Masukkan multiplier, contoh 2.50x",
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.multiplier)

        button = Button(
            text="SIMPAN HASIL RONDE",
            size_hint_y=None,
            height=55
        )
        button.bind(on_press=self.save_result)
        layout.add_widget(button)

        self.history = Label(
            text="Riwayat ronde akan tampil di sini",
            halign="left",
            valign="top"
        )
        layout.add_widget(self.history)

        self.results = []
        return layout

    def save_result(self, instance):
        value = self.multiplier.text.strip()

        try:
            number = float(value.lower().replace("x", ""))

            if number <= 0:
                raise ValueError()

            self.results.append(number)

            self.history.text = "\n".join(
                f"Ronde {i+1}: {v:.2f}x"
                for i, v in enumerate(self.results[-20:])
            )

            self.status.text = "Hasil berhasil disimpan"
            self.multiplier.text = ""

        except ValueError:
            self.status.text = "Masukkan multiplier yang valid"


if __name__ == "__main__":
    SpacemanMonitor().run()
