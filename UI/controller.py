import flet as ft
from UI.view import View
from model.model import Model
from model.corso import Corso


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._id_map_corsi = {}
        self.corso_selezionato = None

    def leggi_corso(self, e):
        self.corso_selezionato = self._view.dd_corso.value

    def populate_dd_corso(self):

        for corso in self._model.get_corsi():
            self._id_map_corsi[corso.codins] = corso
            self._view.dd_corso.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))

        self._view.update_page()


    def cerca_iscritti(self, e):

        if self.corso_selezionato is None:
            self._view.create_alert("Selezionare un corso!")
            return

        #print(self.corso_selezionato)

        iscritti = self._model.get_iscritti_corso(self.corso_selezionato)

        if iscritti is None:
            self._view.create_alert("Problema nella connessione")
            return

        self._view.txt_result.clean()

        if len(iscritti) == 0:
            self._view.txt_result.controls.append(ft.Text("Non ci sono studenti iscritti al corso selezionato"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti al corso:"))
            for studente in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{studente}"))
            self._view.update_page()

    def cerca_studente(self, e):

        matricola = self._view.txt_matricola.value

        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return

        studente = self._model.cerca_studente(int(matricola))

        if studente is None:
            self._view.create_alert("Matricola non presente nel database")
            return
        else:
            self._view.txt_nome.value = f"{studente.nome}"
            self._view.txt_cognome.value = f"{studente.cognome}"

        self._view.update_page()


    def cerca_corsi(self, e):

        matricola = self._view.txt_matricola.value

        if matricola=="":
            self._view.create_alert("Inserire una matricola!")
            return

        corsi = self._model.get_corsi_studente(matricola)

        if len(corsi) == 0:
            self._view.create_alert("La matricola indicata non risulta iscritta a nessun corso")
        else:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi:"))
            for corso in corsi:
                self._view.txt_result.controls.append(ft.Text(f"{corso}"))
            self._view.update_page()

    def iscrivi(self, e):

         matricola = int(self._view.txt_matricola.value)

         if matricola == "":
             self._view.create_alert("Inserire una matricola!")
             return

         studente = self._model.cerca_studente(matricola)

         if studente is None:
             self._view.create_alert("Matricola non presente nel database")
             return

         codice_corso = self._view.dd_corso.value

         if codice_corso is None:
             self._view.create_alert("Selezionare un corso")
             return


         result = self._model.iscrivi_corso(matricola, codice_corso)

         self._view.txt_result.controls.clear()

         if result:
             self._view.txt_result.controls.append(ft.Text("Iscrizione avvenuta con successo!"))
         else:
             self._view.txt_result.controls.append(ft.Text("Iscrizione fallita"))

         self._view.update_page()



