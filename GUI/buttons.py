__author__ = 'Хрюнделя'
from tkinter import *


class DBButton(Button):
    className = 'DBButton'
    bg = "cyan4"
    font = ("georgia", 12)

    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, text=self.className, **config)
        self.pack(fill=BOTH, expand=1)
        self.config(command=self.callback, fg="white", bg=self.bg, font=self.font, bd=5, relief=RAISED)

    def callback(self):
        print(self.className)


class ModeButton(DBButton):
    bg = "#717D7D"
    font = ("georgia", 8)
    className = 'ModeButton'
    width = 60
    def __init__(self, parent=None, **config):
        DBButton.__init__(self, parent, **config)
        self.pack(side=LEFT)
        self.config(width=self.width)


class QueryButton(ModeButton):
    className = "поиск по базе"


class EditButton(ModeButton):
    className = "редактирование базы"


class EntityButton(DBButton):
    className = 'EntityButton'

    def __init__(self, parent=None):
        DBButton.__init__(self, parent)


class DoctorButton(EntityButton):
    className = "врачи"


class OtherPersonalButton(EntityButton):
    className = 'обслуживающий персонал'


class PatientButton(EntityButton):
    className = 'пациенты'


class HospitalButton(EntityButton):
    className = 'больницы'


class PolyclinicButton(EntityButton):
    className = 'поликлиники'


class LaboratoryButton(EntityButton):
    className = 'лаборатории'


if __name__ == '__main__':
    root = Tk()
    DBButton(root)
    ModeButton(root)
    QueryButton(root)
    EditButton(root)
    EntityButton(root)
    DoctorButton(root)
    OtherPersonalButton(root)
    PatientButton(root)
    HospitalButton(root)
    PolyclinicButton(root)
    LaboratoryButton(root)
    root.mainloop()
