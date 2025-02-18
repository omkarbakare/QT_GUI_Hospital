# import sys
# from PySide6.QtCore import QSize, Qt
# from PySide6.QtWidgets import *
# # from design import Ui_Dialog
# # # from PyQt6 import uic
# from PySide6.QtGui import QIcon
# from test_design import Ui_MainWindow

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # uic.loadUi("myDesign.ui", self)  # Load the UI file

#         # self.initUI()
        
#     # def __init__(self):
#     #     super().__init__()

#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
        
#         # self.tabs = QTabWidget(self)
#         # self.setCentralWidget(self.tabs)
#         # Create a Layout for the Container
#         # scroll_area = QScrollArea()
#         # scroll_area.setWidgetResizable(True)  # Allows resizing of content

#         # # Create a Container Widget
#         container = QWidget()
#         # scroll_area.setWidget(container)  # Add container inside scroll area
#         self.ui.scrollArea_2.setWidget(container)
#         # # Create a Layout for the Container
#         layout = QVBoxLayout(container)
#         # layout = QVBoxLayout(container)

#         # Add Multiple Widgets (Example: Labels)
#         for i in range(50):
#             label = QLabel(f"Item {i+1}")
#             layout.addWidget(label)
            
#         # self.ui.tabWidget.addTab(self.ui.scrollArea_2, "Tab_test")
#         self.ui.tabWidget.removeTab(0)
#         self.ui.tabWidget.insertTab(0, self.ui.scrollArea_2, "new tab")
#     # # Add Tabs with Scroll Areas
#     #     self.add_scrollable_tab("Tab 1", 50)  # Add 50 widgets in Tab 1
#     #     self.add_scrollable_tab("Tab 2", 30)  # Add 30 widgets in Tab 2

#     def add_scrollable_tab(self, title, widget_count):
#         """Create a tab with a scrollable area."""
#         # Create Scroll Area
#         scroll_area = QScrollArea()
#         scroll_area.setWidgetResizable(True)  # Allows resizing of content

#         # Create a Container Widget
#         container = QWidget()
#         scroll_area.setWidget(container)  # Add container inside scroll area

#         # Create a Layout for the Container
#         layout = QVBoxLayout(container)

#         # Add Multiple Widgets (Example: Labels)
#         for i in range(widget_count):
#             label = QLabel(f"Item {i+1}")
#             layout.addWidget(label)

#         # Add the Scroll Area as a New Tab
#         self.tabs.addTab(scroll_area, title)
    
    
    
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())



from PyQt6.QtWidgets import *
from PyQt6 import uic
import sys
from test_design import Ui_MainWindow
# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtGui import QIcon

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class ScrollableTab(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        # uic.loadUi("fgfdgfdgd.ui", self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Get the scroll area and container from the UI
        # self.scroll_area = self.findChild(QScrollArea, "scrollArea")  # Get QScrollArea
        # self.scroll_container = self.findChild(QWidget, "scrollAreaWidgetContents")  # Get the inner QWidget
        # self.layout = self.scroll_container.layout()  # Get its layout (must be set in Designer)
        
        # self.tabww = self.findChild(QTabWidget, "tabWidget")
        
        # Ensure the scroll area resizes dynamically
        # self.scroll_area.setWidgetResizable(True)

        # # Find the button and connect it to add new widgets
        # self.add_button = self.findChild(QPushButton, "pushButton")  # Get QPushButton
        # self.add_button.clicked.connect(self.add_new_widget)
        #    Add Multiple Widgets (Example: Labels)
            
        # container = QWidget()
        # self.ui.scrollArea_2.setWidget(self.ui.widget_2)
        # layout = QVBoxLayout(container)
        
        # self.layout = self.ui.scrollArea_2.layout()
        
        # layout.addWidget(self.ui)
        # for i in range(50):
        #     label = QLabel(f"Item {i+1}")
        #     layout.addWidget(label)
        
        # self.ui.tabWidget.addTab(self.ui.scrollArea_2, "Tab_test")
        # self.ui.tabWidget.removeTab(0) 
        # self.ui.tabWidget.insertTab(0, self.ui.scrollArea_2, "new tab")
        size = 10
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
            layout_1 = QHBoxLayout()

            button1 = QPushButton(self)
            button2 = QPushButton(self)
            
            button1.setFixedSize(25, 25)
            button2.setFixedSize(25, 25)
            
            # self.ui.tableComplaint.setCellWidget(self.currentRowCount, 5, button1)
            button1.setIcon(QIcon("C:\\Work\\code\\delete_icon.png"))
            button1.setIconSize(QSize(30,30))
            
            button2.setIcon(QIcon("C:\\Work\\code\\download-6155763_1280.webp"))
            button2.setIconSize(QSize(30,30))
            
            layout_1.addWidget(button1)
            layout_1.addWidget(button2)
            layout_1.setContentsMargins(0, 0, 0, 0)  # Remove margins to fit the buttons within the cell
            cell_widget.setLayout(layout_1)

            self.ui.tableComplaint.setCellWidget(self.currentRowCount, 5, cell_widget)
            
    def add_new_widget(self):
        """Dynamically add new widgets inside the scrollable tab."""
        new_widget = QWidget()  # Create a new QWidget
        new_layout = QVBoxLayout(new_widget)  # Apply a layout
        label = QLabel(f"New Widget {self.layout.count() + 1}")  # Example label
        new_layout.addWidget(label)  # Add the label to the new widget
        self.layout.addWidget(new_widget)  # Add the new widget to the scroll area container

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScrollableTab()
    window.show()
    sys.exit(app.exec())