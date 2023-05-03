# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inteface_productRZQScR.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1219, 665)
        icon = QIcon()
        icon.addFile(u":/icon/Icons/Plano de Fundo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: transparent;")
        MainWindow.setIconSize(QSize(30, 30))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_menubar = QPushButton(self.header_left_frame)
        self.btn_menubar.setObjectName(u"btn_menubar")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.btn_menubar.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menubar.setIcon(icon1)
        self.btn_menubar.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.btn_menubar)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft)

        self.header_main_frame = QFrame(self.header_frame)
        self.header_main_frame.setObjectName(u"header_main_frame")
        self.header_main_frame.setStyleSheet(u"color: white;")
        self.header_main_frame.setFrameShape(QFrame.StyledPanel)
        self.header_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_main_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.header_main_frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setPixmap(QPixmap(u":/Icons/Icons/user-plus.svg"))

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignRight)

        self.label = QLabel(self.header_main_frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.header_main_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_minimizar = QPushButton(self.header_right_frame)
        self.btn_minimizar.setObjectName(u"btn_minimizar")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/divide-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimizar.setIcon(icon2)
        self.btn_minimizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_minimizar)

        self.btn_maximizar = QPushButton(self.header_right_frame)
        self.btn_maximizar.setObjectName(u"btn_maximizar")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximizar.setIcon(icon3)
        self.btn_maximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_maximizar)

        self.btn_close = QPushButton(self.header_right_frame)
        self.btn_close.setObjectName(u"btn_close")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon4)
        self.btn_close.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setStyleSheet(u"\n"
"border-radius: 7px;")
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_menu_contents_frame = QFrame(self.main_body_frame)
        self.left_menu_contents_frame.setObjectName(u"left_menu_contents_frame")
        self.left_menu_contents_frame.setMinimumSize(QSize(70, 0))
        self.left_menu_contents_frame.setMaximumSize(QSize(80, 16777215))
        self.left_menu_contents_frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.left_menu_contents_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_contents_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.left_menu_contents_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_contents_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(220, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_register = QPushButton(self.menu_frame)
        self.btn_register.setObjectName(u"btn_register")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Icons/key.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_register.setIcon(icon5)
        self.btn_register.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_register, 1, 0, 1, 1, Qt.AlignLeft)

        self.btn_database = QPushButton(self.menu_frame)
        self.btn_database.setObjectName(u"btn_database")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_database.setIcon(icon6)
        self.btn_database.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_database, 2, 0, 1, 1, Qt.AlignLeft)

        self.btn_home = QPushButton(self.menu_frame)
        self.btn_home.setObjectName(u"btn_home")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon7)
        self.btn_home.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_home, 0, 0, 1, 1, Qt.AlignLeft)

        self.label_home = QLabel(self.menu_frame)
        self.label_home.setObjectName(u"label_home")
        self.label_home.setFont(font2)
        self.label_home.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_home.setMargin(5)

        self.gridLayout.addWidget(self.label_home, 0, 1, 1, 1, Qt.AlignLeft)

        self.btn_abount = QPushButton(self.menu_frame)
        self.btn_abount.setObjectName(u"btn_abount")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/Icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_abount.setIcon(icon8)
        self.btn_abount.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_abount, 3, 0, 1, 1, Qt.AlignLeft)

        self.label_register = QLabel(self.menu_frame)
        self.label_register.setObjectName(u"label_register")
        self.label_register.setFont(font2)
        self.label_register.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_register.setMargin(5)

        self.gridLayout.addWidget(self.label_register, 1, 1, 1, 1, Qt.AlignLeft)

        self.label_database = QLabel(self.menu_frame)
        self.label_database.setObjectName(u"label_database")
        self.label_database.setFont(font2)
        self.label_database.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_database.setMargin(5)

        self.gridLayout.addWidget(self.label_database, 2, 1, 1, 1, Qt.AlignLeft)

        self.label_abount = QLabel(self.menu_frame)
        self.label_abount.setObjectName(u"label_abount")
        self.label_abount.setFont(font2)
        self.label_abount.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_abount.setMargin(5)

        self.gridLayout.addWidget(self.label_abount, 3, 1, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_8.addWidget(self.left_menu_contents_frame)

        self.main_body_contents = QFrame(self.main_body_frame)
        self.main_body_contents.setObjectName(u"main_body_contents")
        self.main_body_contents.setStyleSheet(u"background-color: rgb(172, 139, 255);")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_12 = QVBoxLayout(self.page_home)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.img_home_frame = QFrame(self.page_home)
        self.img_home_frame.setObjectName(u"img_home_frame")
        self.img_home_frame.setFrameShape(QFrame.StyledPanel)
        self.img_home_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.img_home_frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.img_home = QLabel(self.img_home_frame)
        self.img_home.setObjectName(u"img_home")
        self.img_home.setFrameShape(QFrame.NoFrame)
        self.img_home.setPixmap(QPixmap(u":/Icons/Icons/logo.png"))

        self.horizontalLayout_14.addWidget(self.img_home, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_12.addWidget(self.img_home_frame, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_home_frame = QFrame(self.page_home)
        self.label_home_frame.setObjectName(u"label_home_frame")
        self.label_home_frame.setFrameShape(QFrame.StyledPanel)
        self.label_home_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.label_home_frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, -1)
        self.label_home_2 = QLabel(self.label_home_frame)
        self.label_home_2.setObjectName(u"label_home_2")
        font3 = QFont()
        font3.setPointSize(30)
        font3.setBold(True)
        self.label_home_2.setFont(font3)
        self.label_home_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 100);")

        self.horizontalLayout_13.addWidget(self.label_home_2, 0, Qt.AlignBottom)


        self.verticalLayout_12.addWidget(self.label_home_frame, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.stackedWidget.addWidget(self.page_home)
        self.page_register = QWidget()
        self.page_register.setObjectName(u"page_register")
        self.verticalLayout_9 = QVBoxLayout(self.page_register)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.nome_da_pag = QFrame(self.page_register)
        self.nome_da_pag.setObjectName(u"nome_da_pag")
        self.nome_da_pag.setFrameShape(QFrame.StyledPanel)
        self.nome_da_pag.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.nome_da_pag)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.nome_pag_frame = QFrame(self.nome_da_pag)
        self.nome_pag_frame.setObjectName(u"nome_pag_frame")
        self.nome_pag_frame.setFrameShape(QFrame.StyledPanel)
        self.nome_pag_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.nome_pag_frame)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_nome_pag = QLabel(self.nome_pag_frame)
        self.label_nome_pag.setObjectName(u"label_nome_pag")
        font4 = QFont()
        font4.setPointSize(40)
        font4.setBold(True)
        self.label_nome_pag.setFont(font4)
        self.label_nome_pag.setStyleSheet(u"color: white;")

        self.horizontalLayout_20.addWidget(self.label_nome_pag)


        self.horizontalLayout_10.addWidget(self.nome_pag_frame, 0, Qt.AlignLeft)

        self.salvar_produtos_frame = QFrame(self.nome_da_pag)
        self.salvar_produtos_frame.setObjectName(u"salvar_produtos_frame")
        self.salvar_produtos_frame.setFrameShape(QFrame.StyledPanel)
        self.salvar_produtos_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.salvar_produtos_frame)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, -1, 0)
        self.btn_salvar_produtos = QPushButton(self.salvar_produtos_frame)
        self.btn_salvar_produtos.setObjectName(u"btn_salvar_produtos")
        self.btn_salvar_produtos.setFont(font2)
        self.btn_salvar_produtos.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 100);\n"
"selection-background-color: rgb(35, 169, 181);")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/Icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar_produtos.setIcon(icon9)
        self.btn_salvar_produtos.setIconSize(QSize(40, 40))

        self.horizontalLayout_21.addWidget(self.btn_salvar_produtos)


        self.horizontalLayout_10.addWidget(self.salvar_produtos_frame, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.nome_da_pag)

        self.departamento = QFrame(self.page_register)
        self.departamento.setObjectName(u"departamento")
        self.departamento.setFrameShape(QFrame.StyledPanel)
        self.departamento.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.departamento)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, -1, 0)
        self.label_departamento_lineEdit = QVBoxLayout()
        self.label_departamento_lineEdit.setSpacing(0)
        self.label_departamento_lineEdit.setObjectName(u"label_departamento_lineEdit")
        self.label_departamento = QLabel(self.departamento)
        self.label_departamento.setObjectName(u"label_departamento")
        self.label_departamento.setFont(font2)
        self.label_departamento.setStyleSheet(u"color: white;")

        self.label_departamento_lineEdit.addWidget(self.label_departamento)

        self.lineEdit_departamento = QLineEdit(self.departamento)
        self.lineEdit_departamento.setObjectName(u"lineEdit_departamento")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_departamento.sizePolicy().hasHeightForWidth())
        self.lineEdit_departamento.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setPointSize(15)
        font5.setItalic(True)
        self.lineEdit_departamento.setFont(font5)
        self.lineEdit_departamento.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_departamento.setClearButtonEnabled(True)

        self.label_departamento_lineEdit.addWidget(self.lineEdit_departamento)


        self.verticalLayout_6.addLayout(self.label_departamento_lineEdit)


        self.verticalLayout_9.addWidget(self.departamento)

        self.cod_barras = QFrame(self.page_register)
        self.cod_barras.setObjectName(u"cod_barras")
        self.cod_barras.setFrameShape(QFrame.StyledPanel)
        self.cod_barras.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.cod_barras)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, -1, 0)
        self.label_cod_barras = QLabel(self.cod_barras)
        self.label_cod_barras.setObjectName(u"label_cod_barras")
        self.label_cod_barras.setFont(font2)
        self.label_cod_barras.setStyleSheet(u"color: white;")

        self.verticalLayout_8.addWidget(self.label_cod_barras)

        self.lineEdit_codigo_barras = QLineEdit(self.cod_barras)
        self.lineEdit_codigo_barras.setObjectName(u"lineEdit_codigo_barras")
        sizePolicy1.setHeightForWidth(self.lineEdit_codigo_barras.sizePolicy().hasHeightForWidth())
        self.lineEdit_codigo_barras.setSizePolicy(sizePolicy1)
        self.lineEdit_codigo_barras.setFont(font5)
        self.lineEdit_codigo_barras.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_codigo_barras.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_codigo_barras.setClearButtonEnabled(True)

        self.verticalLayout_8.addWidget(self.lineEdit_codigo_barras)


        self.verticalLayout_9.addWidget(self.cod_barras)

        self.codigo = QFrame(self.page_register)
        self.codigo.setObjectName(u"codigo")
        self.codigo.setFrameShape(QFrame.StyledPanel)
        self.codigo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.codigo)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, -1, 0)
        self.label_codigo_lineEdit = QVBoxLayout()
        self.label_codigo_lineEdit.setSpacing(0)
        self.label_codigo_lineEdit.setObjectName(u"label_codigo_lineEdit")
        self.label_codigo = QLabel(self.codigo)
        self.label_codigo.setObjectName(u"label_codigo")
        font6 = QFont()
        font6.setPointSize(20)
        font6.setBold(True)
        font6.setItalic(False)
        self.label_codigo.setFont(font6)
        self.label_codigo.setStyleSheet(u"color: white;")

        self.label_codigo_lineEdit.addWidget(self.label_codigo)

        self.lineEdit_codigo = QLineEdit(self.codigo)
        self.lineEdit_codigo.setObjectName(u"lineEdit_codigo")
        sizePolicy1.setHeightForWidth(self.lineEdit_codigo.sizePolicy().hasHeightForWidth())
        self.lineEdit_codigo.setSizePolicy(sizePolicy1)
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(False)
        font7.setItalic(True)
        self.lineEdit_codigo.setFont(font7)
        self.lineEdit_codigo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_codigo.setClearButtonEnabled(True)

        self.label_codigo_lineEdit.addWidget(self.lineEdit_codigo)


        self.verticalLayout_7.addLayout(self.label_codigo_lineEdit)


        self.verticalLayout_9.addWidget(self.codigo)

        self.nome_produto = QFrame(self.page_register)
        self.nome_produto.setObjectName(u"nome_produto")
        self.nome_produto.setFrameShape(QFrame.StyledPanel)
        self.nome_produto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.nome_produto)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, -1, 0)
        self.label_nome_produto_lineEdit = QVBoxLayout()
        self.label_nome_produto_lineEdit.setSpacing(0)
        self.label_nome_produto_lineEdit.setObjectName(u"label_nome_produto_lineEdit")
        self.label_nome_produto = QLabel(self.nome_produto)
        self.label_nome_produto.setObjectName(u"label_nome_produto")
        self.label_nome_produto.setFont(font2)
        self.label_nome_produto.setStyleSheet(u"color: white;")

        self.label_nome_produto_lineEdit.addWidget(self.label_nome_produto)

        self.lineEdit_nome_produto = QLineEdit(self.nome_produto)
        self.lineEdit_nome_produto.setObjectName(u"lineEdit_nome_produto")
        sizePolicy1.setHeightForWidth(self.lineEdit_nome_produto.sizePolicy().hasHeightForWidth())
        self.lineEdit_nome_produto.setSizePolicy(sizePolicy1)
        self.lineEdit_nome_produto.setFont(font5)
        self.lineEdit_nome_produto.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_nome_produto.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_nome_produto.setClearButtonEnabled(True)

        self.label_nome_produto_lineEdit.addWidget(self.lineEdit_nome_produto)


        self.verticalLayout_4.addLayout(self.label_nome_produto_lineEdit)


        self.verticalLayout_9.addWidget(self.nome_produto)

        self.preco = QFrame(self.page_register)
        self.preco.setObjectName(u"preco")
        self.preco.setFrameShape(QFrame.StyledPanel)
        self.preco.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.preco)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.label_preco_lineEdit = QVBoxLayout()
        self.label_preco_lineEdit.setSpacing(0)
        self.label_preco_lineEdit.setObjectName(u"label_preco_lineEdit")
        self.label_preco = QLabel(self.preco)
        self.label_preco.setObjectName(u"label_preco")
        self.label_preco.setFont(font2)
        self.label_preco.setStyleSheet(u"color: white;")

        self.label_preco_lineEdit.addWidget(self.label_preco)

        self.lineEdit_preco = QLineEdit(self.preco)
        self.lineEdit_preco.setObjectName(u"lineEdit_preco")
        sizePolicy1.setHeightForWidth(self.lineEdit_preco.sizePolicy().hasHeightForWidth())
        self.lineEdit_preco.setSizePolicy(sizePolicy1)
        self.lineEdit_preco.setFont(font5)
        self.lineEdit_preco.setTabletTracking(False)
        self.lineEdit_preco.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_preco.setClearButtonEnabled(True)

        self.label_preco_lineEdit.addWidget(self.lineEdit_preco)


        self.verticalLayout_3.addLayout(self.label_preco_lineEdit)


        self.verticalLayout_9.addWidget(self.preco)

        self.stackedWidget.addWidget(self.page_register)
        self.page_database = QWidget()
        self.page_database.setObjectName(u"page_database")
        self.verticalLayout_10 = QVBoxLayout(self.page_database)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, 0, 0)
        self.top_database = QFrame(self.page_database)
        self.top_database.setObjectName(u"top_database")
        self.top_database.setFrameShape(QFrame.StyledPanel)
        self.top_database.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.top_database)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.nome_pag_database = QFrame(self.top_database)
        self.nome_pag_database.setObjectName(u"nome_pag_database")
        self.nome_pag_database.setFrameShape(QFrame.StyledPanel)
        self.nome_pag_database.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.nome_pag_database)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.nome_pag_database)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.label_4)


        self.horizontalLayout_15.addWidget(self.nome_pag_database, 0, Qt.AlignLeft)

        self.importar_excel_database = QFrame(self.top_database)
        self.importar_excel_database.setObjectName(u"importar_excel_database")
        self.importar_excel_database.setStyleSheet(u"")
        self.importar_excel_database.setFrameShape(QFrame.StyledPanel)
        self.importar_excel_database.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.importar_excel_database)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btn_save_database = QPushButton(self.importar_excel_database)
        self.btn_save_database.setObjectName(u"btn_save_database")
        self.btn_save_database.setFont(font)
        self.btn_save_database.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 100);\n"
"selection-background-color: rgb(35, 169, 181);")
        self.btn_save_database.setIcon(icon9)
        self.btn_save_database.setIconSize(QSize(25, 25))

        self.horizontalLayout_17.addWidget(self.btn_save_database)


        self.horizontalLayout_15.addWidget(self.importar_excel_database, 0, Qt.AlignRight)

        self.delete_database = QFrame(self.top_database)
        self.delete_database.setObjectName(u"delete_database")
        self.delete_database.setFrameShape(QFrame.StyledPanel)
        self.delete_database.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.delete_database)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 9, 0)
        self.btn_delete_database = QPushButton(self.delete_database)
        self.btn_delete_database.setObjectName(u"btn_delete_database")
        self.btn_delete_database.setFont(font)
        self.btn_delete_database.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 100);\n"
"selection-background-color: rgb(35, 169, 181);")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/Icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_database.setIcon(icon10)
        self.btn_delete_database.setIconSize(QSize(25, 25))

        self.horizontalLayout_19.addWidget(self.btn_delete_database)


        self.horizontalLayout_15.addWidget(self.delete_database, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.top_database, 0, Qt.AlignTop)

        self.database = QFrame(self.page_database)
        self.database.setObjectName(u"database")
        self.database.setFrameShape(QFrame.StyledPanel)
        self.database.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.database)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.database)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(False)
        self.tableWidget.setFont(font8)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(80)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(221)

        self.horizontalLayout_18.addWidget(self.tableWidget)


        self.verticalLayout_10.addWidget(self.database)

        self.stackedWidget.addWidget(self.page_database)
        self.page_abount = QWidget()
        self.page_abount.setObjectName(u"page_abount")
        self.verticalLayout_5 = QVBoxLayout(self.page_abount)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.img_abount = QFrame(self.page_abount)
        self.img_abount.setObjectName(u"img_abount")
        self.img_abount.setFrameShape(QFrame.StyledPanel)
        self.img_abount.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.img_abount)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_img = QLabel(self.img_abount)
        self.label_img.setObjectName(u"label_img")
        self.label_img.setPixmap(QPixmap(u":/Icons/Icons/minha-img.png"))

        self.horizontalLayout_12.addWidget(self.label_img, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.img_abount, 0, Qt.AlignHCenter)

        self.label_abount_text = QFrame(self.page_abount)
        self.label_abount_text.setObjectName(u"label_abount_text")
        self.label_abount_text.setStyleSheet(u"")
        self.label_abount_text.setFrameShape(QFrame.StyledPanel)
        self.label_abount_text.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.label_abount_text)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 9)
        self.label_abount_minha = QLabel(self.label_abount_text)
        self.label_abount_minha.setObjectName(u"label_abount_minha")
        self.label_abount_minha.setFont(font3)
        self.label_abount_minha.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color:rgba(0, 0, 0, 100)")

        self.horizontalLayout_11.addWidget(self.label_abount_minha)


        self.verticalLayout_5.addWidget(self.label_abount_text, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.stackedWidget.addWidget(self.page_abount)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_body_contents)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.footer_frame_left = QFrame(self.footer_frame)
        self.footer_frame_left.setObjectName(u"footer_frame_left")
        self.footer_frame_left.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.footer_frame_left.setFrameShape(QFrame.StyledPanel)
        self.footer_frame_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_frame_left)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.footer_frame_left)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignLeft)


        self.horizontalLayout_7.addWidget(self.footer_frame_left)

        self.footer_frame_right = QFrame(self.footer_frame)
        self.footer_frame_right.setObjectName(u"footer_frame_right")
        self.footer_frame_right.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.footer_frame_right.setFrameShape(QFrame.StyledPanel)
        self.footer_frame_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.footer_frame_right)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton, 0, Qt.AlignRight)


        self.horizontalLayout_7.addWidget(self.footer_frame_right)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DataBase Client", None))
        self.btn_menubar.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cadastramento de Produtos", None))
        self.btn_minimizar.setText("")
        self.btn_maximizar.setText("")
        self.btn_close.setText("")
        self.btn_register.setText("")
        self.btn_database.setText("")
        self.btn_home.setText("")
        self.label_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_abount.setText("")
        self.label_register.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_database.setText(QCoreApplication.translate("MainWindow", u"Dados", None))
        self.label_abount.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.img_home.setText("")
        self.label_home_2.setText(QCoreApplication.translate("MainWindow", u"Sejam Bem-Vindos ao Cadastro de Produtos", None))
        self.label_nome_pag.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Produtos", None))
        self.btn_salvar_produtos.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_departamento.setText(QCoreApplication.translate("MainWindow", u"Departamento:", None))
        self.lineEdit_departamento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira um Departamento", None))
        self.label_cod_barras.setText(QCoreApplication.translate("MainWindow", u"C\u00f3d de Barras:", None))
        self.lineEdit_codigo_barras.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira um Cod. de Barras", None))
        self.label_codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.lineEdit_codigo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira um C\u00f3digo", None))
        self.label_nome_produto.setText(QCoreApplication.translate("MainWindow", u"Nome do Produto:", None))
        self.lineEdit_nome_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira um Nome", None))
        self.label_preco.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o:", None))
        self.lineEdit_preco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ 0.00", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dados", None))
        self.btn_save_database.setText(QCoreApplication.translate("MainWindow", u"Importar para excel", None))
        self.btn_delete_database.setText(QCoreApplication.translate("MainWindow", u"Deletar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo de Barras", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nome do Produto", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Departamento", None));
        self.label_img.setText("")
        self.label_abount_minha.setText(QCoreApplication.translate("MainWindow", u"Meu nome \u00e9 Rafael, sou desenvolvedor independente", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Copyright: Rafael Lacerda", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

