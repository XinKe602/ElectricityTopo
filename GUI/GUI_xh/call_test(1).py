from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QLabel, QHBoxLayout, QMainWindow, \
    QTableWidgetItem, QHeaderView
from PyQt5.uic.properties import QtGui
from PyQt5 import QtCore
from test import Ui_MainWindow
# from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QLabel, QHBoxLayout, QMainWindow
import sys
import pic


class DemoMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 调用Ui_Mainwindow中的函数setupUi实现显示界面
        # self.resize(500, 300)
        # self.label3 = QLabel('No Click')
        # self.tree = QTreeWidget(self)
        # self.tree1.itemClicked.connect(self.change_func)
        pix = QPixmap(':/pic/拓扑图.png')
        self.label_1.setPixmap(pix)
        self.label_1.setScaledContents(True)
        self.treeWidget.itemClicked.connect(self.change_func)
        self.pushButton.clicked.connect(self.treeWidget.expandAll)
        self.pushButton_2.clicked.connect(self.table_func)#初始化的功能


        # self.tableWidget.itemClicked.connect(self.table_func())
        # self.tableWidget.itemClicked().connect()

    def change_func(self, item, column):

        self.textBrowser.setText(item.text(column))
        self.label_2.setText(item.text(column))
        # row1 = self.tableWidget.rowCount()
        # self.tableWidget.insertRow(row1)

        # str(self.tableWidget.item(12,0))
        # item_1 = QTableWidgetItem()
        # self.tableWidget.setItem(row1, 0, item_1)
        # item_2 = QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(row1, item_2)
        # self.label_2.setText(self.tableWidget.item(12,0).text())
        # self.tableWidget.insertRow(row1-1)
        # item1 = self.tableWidget.item(row1, 0)
        # item1.setText(_translate("MainWindow", "信息"))
        # self.tableWidget.item(row1 - 1, 0).setText("1")
        # self.tableWidget.verticalHeaderItem(row1).setText("节点属性")
        # self.tableWidget.removeRow(self.tableWidget.rowCount() - 1)
        topFather = self.treeWidget.currentItem()
        while topFather.parent() is not None:
            topFather = topFather.parent()
        # c=b.indexOfTopLevelItem(b)
        # c=b.indexOfTopLevelItem(b)
        index_father = self.treeWidget.indexOfTopLevelItem(topFather)
        # print(index_father)
        #
        # print(topFather)
        if index_father == 0:
            pix = QPixmap(':/pic/楼1.jpg')
            self.label_1.setPixmap(pix)
            self.label_1.setScaledContents(True)

        elif index_father == 1:
            pix = QPixmap(':/pic/楼2.jpg')
            self.label_1.setPixmap(pix)
            self.label_1.setScaledContents(True)
        elif index_father == 2:
            pix = QPixmap(':/pic/楼3.jpg')
            self.label_1.setPixmap(pix)
            self.label_1.setScaledContents(True)
        elif index_father == 3:
            pix = QPixmap(':/pic/楼4.jpg')
            self.label_1.setPixmap(pix)
            self.label_1.setScaledContents(True)
        else:
            pix = QPixmap(':/pic/拓扑图.png')
            self.label_1.setPixmap(pix)
            self.label_1.setScaledContents(True)

        if item.child(0) is None:  # 没有子节点意味着这是最小的孩子，直接输出该节点的信息
            row1 = self.tableWidget.rowCount()
            num0 = 5
            if num0 < row1:  # 这里进行5个固定行的设置，多删少增

                while num0 < row1:
                    self.tableWidget.removeRow(row1 - 1)
                    row1 = row1 - 1

            elif num0 > row1:

                while row1 < num0:
                    self.tableWidget.insertRow(row1)
                    item_1 = QTableWidgetItem()
                    self.tableWidget.setItem(row1, 0, item_1)
                    item_2 = QTableWidgetItem()
                    self.tableWidget.setVerticalHeaderItem(row1, item_2)
                    row1 = row1 + 1

            else:
                pass

            num1 = 0  # 更改完行数之后直接赋值
            while num1 < self.tableWidget.rowCount():
                self.tableWidget.item(num1, 0).setText(item.text(column) + "数据库里的信息" + str(num1 + 1))  # 循环更改表格内容
                self.tableWidget.verticalHeaderItem(num1).setText("节点属性" + str(num1 + 1))
                num1 = num1 + 1

        else:

            num2 = 0
            while 1:  # 这里是对子节点的个数进行统计
                if item.child(num2) is None:  # 子节点遍历完了话，进行以下操作
                    break

                else:
                    num2 = num2 + 1

            row1 = self.tableWidget.rowCount()

            if num2 < row1:  # 这里还是根据子节点的个数和表格的行数进行比较，进行少增多删

                while num2 < row1:
                    self.tableWidget.removeRow(row1 - 1)
                    row1 = row1 - 1

            elif num2 > row1:

                while row1 < num2:
                    self.tableWidget.insertRow(row1)
                    item_1 = QTableWidgetItem()
                    self.tableWidget.setItem(row1, 0, item_1)
                    item_2 = QTableWidgetItem()
                    self.tableWidget.setVerticalHeaderItem(row1, item_2)
                    row1 = row1 + 1
            else:
                pass

            num3 = 0
            while num3 < num2:
                self.tableWidget.item(num3, 0).setText(item.child(num3).text(column))  # 调整完行数之后进行输出
                self.textBrowser.append(item.child(num3).text(column))
                self.tableWidget.verticalHeaderItem(num3).setText("子节点")
                num3 = num3 + 1

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # 根据字体内容调整表格宽度

    def table_func(self):  # 暂时没用
        self.treeWidget.reset
        pix = QPixmap(':/pic/拓扑图.png')
        self.label_1.setPixmap(pix)
        self.label_1.setScaledContents(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DemoMain()
    demo.show()
    sys.exit(app.exec_())
