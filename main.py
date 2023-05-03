#############################################################################################################################################################################
# Imports
import os
import sys
import sqlite3
import openpyxl
#############################################################################################################################################################################
# Froms
from ui_inteface_product import *
from PySide6.QtWidgets import QMessageBox, QFileDialog, QSizeGrip
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QAbstractAnimation
from PySide6.QtGui import QIcon, QPixmap, QSinglePointEvent
from PySide6 import QtCore
#############################################################################################################################################################################
# Functions
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
#############################################################################################################################################################################
        # Icon Window
        self.setWindowIcon(QIcon(":/Icons/Icons/user-check.svg"))
        self.setWindowTitle('Cadastro de Produtos')
        # Icon Page Home
        pixmap = QPixmap(":/Icons/Icons/logo.png")
        self.ui.img_home.setPixmap(pixmap)
#############################################################################################################################################################################
        # Functions Exportar, Save, Load and Delete
        def exportar_xls():
            
            # Abrir ou criar o arquivo Excel
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            
            # Escrever os dados na planilha
            for row in range(self.ui.tableWidget.rowCount()):
                for col in range(self.ui.tableWidget.colorCount()):
                    cell_item = self.ui.tableWidget.item(row, col)
                    if cell_item is not None:
                        cell_value = cell_item.text()
                        sheet.cell(row=row+1, column=col+1, value=cell_value)
            
            # Salvar o arquivo
            filename, _ = QFileDialog.getSaveFileName(self, 'Exportar para Excel', '', 'Arquivo Excel(*.xls)')
            if filename:
                workbook.save(filename)
                certo()
        
        # Save dados
        def save_product():
            codigo = self.ui.lineEdit_codigo.text()
            codigo_de_barras = self.ui.lineEdit_codigo_barras.text()
            nome_do_produto = self.ui.lineEdit_nome_produto.text()
            preco = self.ui.lineEdit_preco.text()
            departamento = self.ui.lineEdit_departamento.text()
            
            # Connect to database
            conn = sqlite3.connect('products.db')
            c = conn.cursor()
            
            # Create table if it doesn't exist
            c.execute('''CREATE TABLE IF NOT EXISTS produtos 
                        (codigo INTEGER PRIMARY KEY, nome_produto text, codigo_de_barras text, preco text, departamento text)''')
            
            # Read existing data from table
            c.execute("SELECT * FROM produtos")
            existing_data = c.fetchall()
            
            # Add new data to list
            new_data = (codigo, nome_do_produto,
                        codigo_de_barras, preco, departamento)
            all_data = existing_data + [new_data]
            
            # Save data to database
            c.execute("DELETE FROM produtos")
            c.executemany("INSERT INTO produtos VALUES(?, ?, ?, ?, ?)", all_data)
            conn.commit()
            
            # Close database connection
            conn.close()
            
            # Add new line
            row_count =  self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_count)
            
            # Preencher as células
            self.ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(codigo))
            self.ui.tableWidget.setItem(
                row_count, 1, QTableWidgetItem(codigo_de_barras))
            self.ui.tableWidget.setItem(
                row_count, 2, QTableWidgetItem(nome_do_produto))
            self.ui.tableWidget.setItem(row_count, 3, QTableWidgetItem(preco))
            self.ui.tableWidget.setItem(
                row_count, 4, QTableWidgetItem(departamento))
        self.ui.btn_salvar_produtos.clicked.connect(save_product)

        # Load DataBase
        def load_data():
            try:
                conn = sqlite3.connect("products.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM produtos")
                rows = cur.fetchall()

                for row in rows:
                    codigo = row[0]
                    codigo_de_barras = row[1]
                    nome_do_produto = row[2]
                    preco = row[3]
                    departamento = row[4]

                    # Adicionar nova linha
                    row_count = self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.insertRow(row_count)

                    # Preencher as Células
                    self.ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(codigo))
                    self.ui.tableWidget.setItem(row_count, 1, QTableWidgetItem(codigo_de_barras))
                    self.ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(nome_do_produto))
                    self.ui.tableWidget.setItem(row_count, 3, QTableWidgetItem(preco))
                    self.ui.tableWidget.setItem(row_count, 4, QTableWidgetItem(departamento))
                conn.close()

            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
        load_data()

        #delete
        def delete_selected_rows():
            # Obtém os itens selecionados da tableWidget
            selected_items = self.ui.tableWidget.selectedItems()
            if not selected_items:
                return  # Nenhum item selecionado

            # Remove as linhas correspondentes do banco de dados
            conn = sqlite3.connect('products.db')
            c = conn.cursor()
            for item in selected_items:
                row_index = item.row()
                codigo = self.ui.tableWidget.item(row_index, 0).data(QtCore.Qt.DisplayRole)
                c.execute("DELETE FROM produtos WHERE codigo = ?", (codigo,))
            conn.commit()
            conn.close()

            # Remove as linhas selecionadas da tableWidget
            rows_to_remove = set()
            for item in selected_items:
                rows_to_remove.add(item.row())
            for row in sorted(rows_to_remove, reverse=True):
                self.ui.tableWidget.removeRow(row)


        self.ui.btn_delete_database.clicked.connect(delete_selected_rows)
#############################################################################################################################################################################
        # Functions Buttom save
        self.ui.btn_save_database.clicked.connect(exportar_xls)
#############################################################################################################################################################################
        # DialogBox
        def certo():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Sua informção foi Salva")
            msg.setWindowTitle("Banco de Dados")
            msg.exec()
        
        # Buttons
        self.ui.btn_salvar_produtos.clicked.connect(certo)
        self.ui.btn_save_database.clicked.connect(certo)
#############################################################################################################################################################################
        # Function Buttom
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        self.ui.btn_register.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_register))
        self.ui.btn_database.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_database))
        self.ui.btn_abount.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_abount))
#############################################################################################################################################################################
        # Remove Window tittle bar
        self.setWindowFlags(Qt.FramelessWindowHint)       
#############################################################################################################################################################################
        #Size Grip
        QSizeGrip(self.ui.size_grip)
#############################################################################################################################################################################
        # Function Buttoms Close, Minimizar, Maximinizar and Menu_Bar
        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.btn_minimizar.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_maximizar.clicked.connect(
            lambda: self.restore_or_maximize())
        self.ui.btn_menubar.clicked.connect(lambda: self.slidLeftMenu())
#############################################################################################################################################################################
        # Move Window
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.header_frame.mouseMoveEvent = moveWindow
#############################################################################################################################################################################
        # Finalition Program
        self.show()
#############################################################################################################################################################################
    # Function restore and maximize window
    def restore_or_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
#############################################################################################################################################################################
    # Animation Moving Menu Bar
    def slidLeftMenu(self):
        width = self.ui.left_menu_contents_frame.width()
        if width == 80:
            newWidth = 240
        else:
            newWidth = 80

        self.animation = QPropertyAnimation(
            self.ui.left_menu_contents_frame, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.startValue()
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
#############################################################################################################################################################################
    # Event Mouse
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
#############################################################################################################################################################################
# Execute Program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
#############################################################################################################################################################################
