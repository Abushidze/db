from GUI.buttons import *

__author__ = 'Хрюнделя'


class DBFrame(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self,  parent)
        self.configure(background='#F4FFFF')
        self.make_widgets()

    def make_widgets(self):
        pass


class ButtonsFrame(DBFrame):
    def __init__(self, parent=None):
        DBFrame.__init__(self, parent)
        self.pack(side=LEFT, fill=BOTH, expand=YES)


    def make_widgets(self):
        HospitalButton(self)
        PolyclinicButton(self)
        LaboratoryButton(self)
        DoctorButton(self)
        OtherPersonalButton(self)
        PatientButton(self)



class ModeFrame(DBFrame):
    def __init__(self, parent=None):
        DBFrame.__init__(self, parent)
        self.pack(fill=X)

    def make_widgets(self):
        QueryButton(self)
        EditButton(self)


class ContentFrame(DBFrame):
    def __init__(self, parent=None):
        DBFrame.__init__(self, parent)
        self.pack(side=RIGHT, fill=BOTH, expand=YES)

    def make_widgets(self):
        ModeFrame(self)


if __name__ == "__main__":
    root = Tk()

    ButtonsFrame(root)
    ContentFrame(root)

    root.mainloop()