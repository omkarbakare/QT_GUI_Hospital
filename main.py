import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import *
# from design import Ui_Dialog
from design import Ui_MainWindow 
# from PyQt6 import uic
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi("myDesign.ui", self)  # Load the UI file

        # self.initUI()
        
    # def __init__(self):
    #     super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # self.ui.scrollArea.showMaximized()
        
        # self.ui.scrollArea.setWidget(self.ui.tableComplaint)
        # self.ui.scrollArea_2.showMaximized()
        # layout = QVBoxLayout()
        
        # self.ui.tableComplaint.insertRow(1)
        
        size = 10
        self.ui.tableComplaint.horizontalHeader().setFixedHeight(30)
        
        self.ui.tableComplaint.setColumnWidth(0, 20)

        for i in range(1, 11):
            self.currentRowCount = self.ui.tableComplaint.rowCount() # c
            self.ui.tableComplaint.insertRow(self.currentRowCount)
            self.ui.tableComplaint.setRowHeight(i, 50)

            # col_0_width = self.ui.tableComplaint.columnWidth(0)
            # print(f"col_0_width {col_0_width} ")
            # # edit0 = QLineEdit(str(i))
            # # edit0.setFixedSize(col_0_width-size, 25)
            # self.ui.tableComplaint.setCellWidget(self.currentRowCount,0, edit0)
            
            col_2_width = self.ui.tableComplaint.columnWidth(1)
            t_edit1 = QLineEdit()
            # t_edit1.setFixedSize(col_2_width-size, 25)
            self.ui.tableComplaint.setCellWidget(self.currentRowCount,1, t_edit1)
            
            col_3_width = self.ui.tableComplaint.columnWidth(2)
            edit1 = QLineEdit()
            # edit1.setFixedSize(col_3_width-size, 25)
            self.ui.tableComplaint.setCellWidget(self.currentRowCount,2, edit1)
            
            col_4_width = self.ui.tableComplaint.columnWidth(3)
            edit2 = QComboBox()
            edit2.setFixedSize(col_4_width-size, 25)
            self.ui.tableComplaint.setCellWidget(self.currentRowCount,3, edit2)
            
            col_5_width = self.ui.tableComplaint.columnWidth(4)
            edit3 = QLineEdit()
            edit3.setFixedSize(col_5_width-size, 25)
            self.ui.tableComplaint.setCellWidget(self.currentRowCount,4, edit3)
            
            cell_widget = QWidget()
            layout = QHBoxLayout()

            button1 = QPushButton()
            button2 = QPushButton()
            
            button1.setFixedSize(25, 25)
            button2.setFixedSize(25, 25)
            
            # self.ui.tableComplaint.setCellWidget(self.currentRowCount, 5, button1)
            button1.setIcon(QIcon('C:\Work\code\png-clipart-delete-logo-button-icon-delete-button-love-image-file-formats-thumbnail.png'))
            button1.setIconSize(QSize(30,30))
            
            button2.setIcon(QIcon('C:\Work\code\download-6155763_1280.webp'))
            button2.setIconSize(QSize(30,30))
            
            layout.addWidget(button1)
            layout.addWidget(button2)
            layout.setContentsMargins(0, 0, 0, 0)  # Remove margins to fit the buttons within the cell
            cell_widget.setLayout(layout)

            self.ui.tableComplaint.setCellWidget(self.currentRowCount, 5, cell_widget)
            
        
        # cell_widget = QWidget()
        # layout = QHBoxLayout()
        
        # button_setting = QPushButton()
        # button_setting.setFixedSize(25, 25)
        # button_setting.setIcon(QIcon('C:\Work\code\settings-icon.webp'))
        # button_setting.setIconSize(QSize(30,30))
        # layout.addWidget(self.ui.tableWidget_2.horizontalHeaderItem(2))
        # layout.addWidget(button_setting)
        # layout.setContentsMargins(0, 0, 0, 0)  # Remove margins to fit the buttons within the cell
        # cell_widget.setLayout(layout)
            
            header = self.ui.tableWidget_2.horizontalHeader()
            settings_button = QPushButton("⚙")
            settings_button.clicked.connect(self.open_settings)

            # Create a widget to hold the button
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.addWidget(settings_button)
            layout.setContentsMargins(0, 0, 0, 0)
            # layout.setAlignment(settings_button,  AlignCenter)  # Align center

            # Set the widget as the section for the last column
            self.ui.tableWidget_2.setCellWidget(self.currentRowCount, 4, widget)
            header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
            
            self.currentPrescriptionRow = self.ui.tableWidget_2.rowCount() # c
            self.ui.tableWidget_2.insertRow(self.currentPrescriptionRow)
    
    def open_settings(self):
        print("Settings button clicked!")
    # def show(self):
    #     self.show()



app=QApplication(sys.argv)
window=MainWindow()
window.showMaximized()
window.show()
app.exec()