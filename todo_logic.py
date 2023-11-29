from PyQt6.QtWidgets import *
from todo_gui import *

class Logic(QMainWindow, Ui_MainWindow):
    '''
    A class representing the control logic of To-Do list application work
    '''
    def __init__(self) -> None:
        '''
        Constructor to create initial actions of To-Do list application
        '''
        super().__init__()
        self.setupUi(self)

        self.button_add.clicked.connect(lambda : self.add())
        self.button_complete.clicked.connect(lambda : self.complete())
        self.button_return_to_do.clicked.connect(lambda : self.return_to_do())
        self.button_clear_all_to_do.clicked.connect(lambda: self.clear_all_to_do())
        self.button_clear_all_complete.clicked.connect(lambda: self.clear_all_complete())
        self.button_exit.clicked.connect(lambda: self.exit())

        self.to_do_list = []
        self.complete_list = []


    def add(self) -> None:
        '''
        Method to add list to To-Do list
        '''
        add_to_do = self.input_to_do.text()
        if add_to_do:
            self.to_do_list.append(add_to_do)
            self.widget_to_do_list.addItem(add_to_do)
            self.input_to_do.clear()

    def complete(self) -> None:
        '''
        Method to move list of To-Do list to complete list
        '''
        selected_to_do_items = self.widget_to_do_list.selectedItems()

        for item in selected_to_do_items:
            self.to_do_list.remove(item.text())
            self.widget_to_do_list.takeItem(self.widget_to_do_list.row(item))

            self.complete_list.append(item.text())
            self.widget_complete_list.addItem(item.text())


    def return_to_do(self) -> None:
        '''
        Method to return list of complete list to To-Do list
        '''
        selected_complete_items = self.widget_complete_list.selectedItems()

        for item in selected_complete_items:
            self.complete_list.remove(item.text())
            self.widget_complete_list.takeItem(self.widget_complete_list.row(item))

            self.to_do_list.append(item.text())
            self.widget_to_do_list.addItem(item.text())

    def clear_all_to_do(self) -> None:
        '''
        Method to clear To-Do list
        '''
        self.widget_to_do_list.clear()

    def clear_all_complete(self) -> None:
        '''
        Method to clear complete list
        '''
        self.widget_complete_list.clear()

    def exit(self) -> None:
        '''
        Method to terminate To-Do list application
        '''
        QApplication.instance().quit()
