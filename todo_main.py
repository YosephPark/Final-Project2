from todo_logic import *

def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__=='__main__':
    main()