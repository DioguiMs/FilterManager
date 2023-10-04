# ui.main_window.py
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QHBoxLayout, QFileDialog
from PyQt5.QtCore import Qt, QResource, QFile, QTextStream
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5 import QtWidgets, QtCore
from ui.animated_button import AnimatedButton, RunAnimatedButton
from ui.logic import PriceFilter, open_dialog
import os
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self): 
        
        global rogers_file_path 
        global rq_file_path
        
        self.setWindowTitle("FilterManager.exe")
        self.setObjectName("menu")
        self.setFixedSize(430, 558)
        self.menu_widget = QtWidgets.QWidget(self)
        self.menu_widget.setObjectName("menu_widget")
        
        ## Main Layout

        self.verticalLayoutWidget = QtWidgets.QWidget(self.menu_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 160, 341, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setObjectName("main_layout")
        
        # Main Frame

        self.main_frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.main_frame)
        
        # Rogers Pricing Layout
        
        
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.rogers_pricing_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.rogers_pricing_layout.setContentsMargins(0, 0, 0, 0)
        self.rogers_pricing_layout.setObjectName("rogers_pricing_layout")
        self.rogers_pricing_layout.setSpacing(25)

        # Pricing Label

        self.rogers_pricing_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.rogers_pricing_label.setObjectName("rogers_pricing_label")
        self.rogers_pricing_label.setText("Select the Rogers pricing file:") 
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rogers_pricing_label.sizePolicy().hasHeightForWidth())
        self.rogers_pricing_label.setSizePolicy(sizePolicy)
        self.rogers_pricing_label.setMaximumSize(QtCore.QSize(220, 16777215))
        self.rogers_pricing_label.setMinimumSize(QtCore.QSize(220, 0))      
        
        self.rogers_pricing_layout.addWidget(self.rogers_pricing_label) ## Add label to widget
        

        ## Pricing button
        
        self.rogers_pricing_button = AnimatedButton(self.horizontalLayoutWidget)
        self.rogers_pricing_button.setText("...")
        self.rogers_pricing_button.setObjectName("rogers_pricing_button")
        self.rogers_pricing_layout.addWidget(self.rogers_pricing_button)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rogers_pricing_button.sizePolicy().hasHeightForWidth())
        self.rogers_pricing_button.setSizePolicy(sizePolicy)
        self.rogers_pricing_button.setMinimumSize(QtCore.QSize(30, 20))
        self.rogers_pricing_button.setMaximumSize(QtCore.QSize(30, 20))       
    
        ### Spacer
        
        spacerItem = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.rogers_pricing_layout.addItem(spacerItem)

        # Layout
        
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.main_frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 321, 20))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.rogers_path_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.rogers_path_layout.setContentsMargins(0, 0, 0, 0)
        self.rogers_path_layout.setObjectName("rogers_path_layout")

        self.rogers_path_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.rogers_path_label.setObjectName("rogers_path_label")
        self.rogers_path_layout.addWidget(self.rogers_path_label)
        
        self.rogers_path_layout.addStretch(1)
        self.main_layout.addWidget(self.main_frame)
        self.setCentralWidget(self.menu_widget)
        
        spacerItem1 = QtWidgets.QSpacerItem(1, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.rogers_path_layout.addItem(spacerItem1)
        
        
        ##################      Second Layout scheme        ############################
        
        
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.main_frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 120, 321, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.rq_pricing_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.rq_pricing_layout.setContentsMargins(0, 0, 0, 0)
        self.rq_pricing_layout.setSpacing(25)
        self.rq_pricing_layout.setObjectName("rq_pricing_layout")
        
        # RQ Pricing Label
        
        self.rq_pricing_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rq_pricing_label.sizePolicy().hasHeightForWidth())
        self.rq_pricing_label.setSizePolicy(sizePolicy)
        self.rq_pricing_label.setMaximumSize(QtCore.QSize(220, 16777215))
        self.rq_pricing_label.setMinimumSize(QtCore.QSize(220, 0))
        self.rq_pricing_label.setObjectName("rq_pricing_label")
        self.rq_pricing_label.setText("Select the RQ pricing file:")
        self.rq_pricing_layout.addWidget(self.rq_pricing_label)
        
        
        #### RQ Pricing button

        
        self.rq_pricing_button = AnimatedButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rq_pricing_button.sizePolicy().hasHeightForWidth())
        self.rq_pricing_button.setSizePolicy(sizePolicy)
        self.rq_pricing_button.setMinimumSize(QtCore.QSize(30, 20))
        self.rq_pricing_button.setMaximumSize(QtCore.QSize(30, 20))        
        self.rq_pricing_button.setObjectName("rq_pricing_button")
        self.rq_pricing_button.setText("...")
        self.rq_pricing_layout.addWidget(self.rq_pricing_button)       
        
        
        spacerItem2 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.rq_pricing_layout.addItem(spacerItem2)
        
        
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.main_frame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 160, 321, 20))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.rq_path_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.rq_path_layout.setContentsMargins(0, 0, 0, 0)
        self.rq_path_layout.setSpacing(0)
        self.rq_path_layout.setObjectName("rq_path_layout")
        
        self.rq_path_label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.rq_path_label.setMaximumSize(QtCore.QSize(1666662, 16777215))
        self.rq_path_label.setObjectName("rq_path_label")
        self.rq_path_layout.addWidget(self.rq_path_label)
        spacerItem3 = QtWidgets.QSpacerItem(1, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.rq_path_layout.addItem(spacerItem3)
        
        
        
        
        
        #######################     Run Layout Scheme       ###########################
        
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 210, 120, 50))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.run_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.run_layout.setContentsMargins(0, 0, 0, 0)
        self.run_layout.setObjectName("run_layout")
        
        self.run_button = RunAnimatedButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.rq_pricing_button.sizePolicy().hasHeightForWidth())
        self.rq_pricing_button.setSizePolicy(sizePolicy)   
        self.run_button.setObjectName("run_button")
        self.run_button.setText("Run")
        self.run_button.setFixedHeight(50)
        self.run_layout.addWidget(self.run_button)

        QtCore.QMetaObject.connectSlotsByName(self)
        
        ####################################################################################
        
########################### Imagine Wireless icon

        self.label = QtWidgets.QLabel(self.menu_widget)
        self.label.setGeometry(QtCore.QRect(0, 20, 171, 71))
        self.label.setText("")
        self.label.setPixmap(QPixmap(":/styles/assets/bin/Imagine Wireless (Dark Mode).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
########################### Window icon

        self.setWindowIcon(QIcon(":/styles/assets/bin/icon.png"))
        
        
        
        
        
        
        
        ###################### Button actions ########################


        #### Rogers button action
        
        self.rogers_pricing_button.clicked.connect(lambda: self.open_file_dialog("rogers", self.rq_pricing_button, self.rogers_path_label, self.rq_path_label))        
        
        
        ### RQ button action
                
        self.rq_pricing_button.clicked.connect(lambda: self.open_file_dialog("rq", self.rq_pricing_button, self.rogers_path_label, self.rq_path_label))

        
        ## Run button action
        
        self.run_button.clicked.connect(lambda: self.filter_function())
        
                
        
        
    def open_file_dialog(self, button_name, button, rogers_path_label, rq_path_label):
        
        file_filter = "Excel files (*.xlsx *.xls);;All files (*)"     
            
        if button_name == "rogers":
            
            open_dialog(self, button_name, button, file_filter, rogers_path_label, rq_path_label)        
            
            
        if button_name == "rq":
            
            open_dialog(self, button_name, button, file_filter, rogers_path_label, rq_path_label)        

        
        
    def filter_function(self):
        PriceFilter(self)
