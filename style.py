def resultBtnStyle():
    return """
        QPushButton {
        background-color: #08729A;
        border-style: outset;
        border-width: 2px;
        border-radius: 8px;
        border-color: #052D3D;
        font: 12px;
        padding: 1px;
        min-width: 2em;
        }
            """

def displayStyle():
    return """
            QLabel {
            font: 11pt Times Bold;
            color: #052D3D;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: 0 #08729A, stop: 1 white);
            gridline-color: black;
            }
                """

def textStyle():
    return """
    QComboBox {
            selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: 0.7 #6D8CFD , stop: 0 white);
            font: 9pt Times Bold;
            }
            """

def resultLabelStyle():
    return """
    QLabel{
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: 0.7 #6D8CFD , stop: 0 white);
            font: 11pt Times Bold;
            }
            """

def lineEditStyle():
    return """
    QLineEdit{
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: 0.7 #6D8CFD , stop: 0 white);
            font: 11pt Times Bold;
            }
            """
def toolTipStyle():
    return """
    QToolTip { 
            font: 11pt Times Bold;
            color: black;
            border-style: outset;
            border-width: 2px;
            border-radius: 8px;
            border-color: #052D3D;
            font: 12px;
            padding: 1px;
            min-width: 2em;
            }
            """

def textLabelstyle():
    return """    
    QLabel{ font: 11pt Times Bold;
            color: #052D3D;
            }
            """