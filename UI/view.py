import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - Segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_corso = None
        self.btn_cerca_iscritti = None
        self.txt_matricola = None
        self.txt_nome = None
        self.txt_cognome = None
        self.btn_cerca_studente = None
        self.btn_cerca_corsi = None
        self.btn_iscrivi = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        self.dd_corso = ft.Dropdown(label="corso", hint_text="Selezionare un corso", width=550, options=[], autofocus=True, on_change=self._controller.leggi_corso)
        self._controller.populate_dd_corso()
        self.btn_cerca_iscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.cerca_iscritti, tooltip="Cerca gli iscritti al corso selezionato")

        row0 = ft.Row([self.dd_corso, self.btn_cerca_iscritti], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row0)


        self.txt_matricola = ft.TextField(label="matricola", width=150, hint_text="Inserire matricola")
        self.txt_nome = ft.TextField(label="nome", width=250, read_only=True)
        self.txt_cognome = ft.TextField(label="cognome", width=250, read_only=True)

        row1 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)


        self.btn_cerca_studente = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.cerca_studente, tooltip="Verifica se c'è uno studente con la matricola specificata" )
        self.btn_cerca_corsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.cerca_corsi, tooltip="Cerca i corsi a cui è iscritto lo studente con la matricola specificata")
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.iscrivi, tooltip="Iscrive al corso selezionato lo studente con la matricola specificata")

        row2 = ft.Row([self.btn_cerca_studente, self.btn_cerca_corsi, self.btn_iscrivi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)

        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)

        self.update_page()


    @property
    def controller(self):
        return self._controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
