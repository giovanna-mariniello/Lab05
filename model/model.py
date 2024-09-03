from database import corso_DAO
from database import studente_DAO

class Model:

   def get_corsi(self):
       return corso_DAO.get_corsi()

   def get_iscritti_corso(self, codins):
       return corso_DAO.get_iscritti_corso(codins)

   def cerca_studente(self, matricola):
       return studente_DAO.cerca_studente(matricola)

   def get_corsi_studente(self, matricola):
       return corso_DAO.get_corsi_studente(matricola)

   def iscrivi_corso(self, matricola, codins):
       return corso_DAO.iscrivi_corso(matricola, codins)
