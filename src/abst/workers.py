from time import sleep

from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal

from abst.helper import get_data_from_key


class Worker_NIBD(QObject):
    finished = pyqtSignal()

    def __init__(self, parent) -> None:
        self.parent = parent
        super(Worker_NIBD, self).__init__()

    def run(self) -> None:
        self.get_data_nibd(self.parent)
        self.finished.emit()

    def get_data_nibd(self, parent) -> None:
        # Farbe zu gelb
        parent.BTN_NIBD.setEnabled(False)
        parent.BTN_NIBD.setStyleSheet('background-color: yellow')
        # Sound abspielen und warten
        self.nibd_sound_and_wait()
        # get Data
        syst = get_data_from_key("systole")
        dias = get_data_from_key("diastole")
        # set Text
        parent.TXT_NIBD_Sys.setText(str(syst))
        parent.TXT_NIBD_Dia.setText(str(dias))
        parent.TXT_NIBD_Sys.setStyleSheet(f'background-color: {"lightblue"}')
        parent.TXT_NIBD_Dia.setStyleSheet(f'background-color: {"lightblue"}')
        sleep(0.4)
        parent.TXT_NIBD_Sys.setStyleSheet(f'background-color: {"transparent"}')
        parent.TXT_NIBD_Dia.setStyleSheet(f'background-color: {"transparent"}')

        # Farbe zu Grün
        parent.BTN_NIBD.setStyleSheet(f'background-color: {parent.farbe_ein}')
        parent.BTN_NIBD.setEnabled(True)

    def nibd_sound_and_wait(self) -> None:
        # Todo play Sound
        # Todo anpassen des warte intervalls
        sleep(5)
