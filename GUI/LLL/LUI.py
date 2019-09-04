from PyQt5.QtCore import Qt
# from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import treePlotter
from treePlotter import __init__
from UIL import Ui_MainWindow
from PyQt5.QtWidgets import QTreeWidgetItem, QHeaderView, QGridLayout
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import (QWidget,QTableWidget,QHBoxLayout,QApplication,QTableWidgetItem,QMainWindow)
from PyQt5 import QtWidgets
import sys
import sip
#传入数据
group1List=[{'address':'101','Pa':11},{'address':'102','Pa':12},
            {'address':'103','Pa':13},{'address':'104','Pa':14}]
group2List=[
            {'address':'201','Pa':15},{'address':'202','Pa':16},
            {'address':'203','Pa':17},{'address':'204','Pa':18}]
listOfTrees = [{'101': {0: '102', 1: {'node': {0: '103', 1: '104'}}}},
                {'201': {0: '203', 1: {'node': {0: '203', 1: '204'}}}}
                ]
class myWindow(QtWidgets.QWidget,Ui_MainWindow):
    # 分组信息存储
    grouplist = []
    # 用户信息存储
    userslist = []
    def __init__(self):
        super(myWindow,self).__init__()
        self.setupUi(self)
        self.Ui_init()
        # self.Ui_initTable()
    def Ui_init(self):
        # 目录初始化
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setColumnWidth(0, 50)
        self.treeWidget.setHeaderLabels(["分组"])
        self.treeWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # 表格初始化
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        newItem1 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, newItem1)
        newItem2 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, newItem2)
        QTableWidget.resizeColumnsToContents(self.tableWidget)
        QTableWidget.resizeRowsToContents(self.tableWidget)
        root1 = self.creategroup('group1',group1List)
        root1.setExpanded(False)
        root2 = self.creategroup('group2',group2List)
        root2.setExpanded(False)
        fig = plt.figure()
        self.canvas = FigureCanvas(fig)
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.canvas, 0, 1)
        self.treeWidget.itemClicked.connect(self.isclick)
    def creategroup(self, groupname,childList):
        group = QTreeWidgetItem(self.treeWidget)
        groupdic = {'group': group, 'groupname': groupname}
        resultList = [x['address'] for x in childList]
        for i in resultList:
            child = QTreeWidgetItem()
            randname = i
            userdic = {'user': child, 'username': randname}
            self.userslist.append(userdic)
            child.setText(0, randname)
            child.setTextAlignment(0, Qt.AlignHCenter | Qt.AlignVCenter)
            group.addChild(child)
        group.setText(0, groupname)
        self.grouplist.append(groupdic)
        return group
    def isclick(self, item,column):
        # 最小的节点，输出节点信息

        global pa
        if item.child(0) is None:
            if self.tableWidget.item(0,1)is None:
                self.tableWidget.insertColumn(1)
                newItem3 = QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(1, newItem3)
                self.tableWidget.horizontalHeaderItem(1).setText("功率")
                newItem4 = QTableWidgetItem()
                self.tableWidget.setItem(0, 1, newItem4)
            for i in range(len(group1List)):
                    if item.text(column)==group1List[i]['address']:
                        pa=str(group1List[i]['Pa'])
                        break
            for i in range(len(group2List)):
                    if item.text(column) == group2List[i]['address']:
                        pa = str(group2List[i]['Pa'])
                        break
            self.tableWidget.item(0, 0).setText(item.text(column))
            self.tableWidget.item(0, 1).setText(pa)
        else:
            self.tableWidget.removeColumn(1)
            self.tableWidget.item(0, 0).setText(item.text(column))
            # if item.text
            topFather = self.treeWidget.currentItem()
            index_father = self.treeWidget.indexOfTopLevelItem(topFather)
            if index_father == 0:
                sip.delete(self.canvas)
                self.canvas = FigureCanvas(self.createPlot(self.retrieveTree(0)))
                self.gridlayout.addWidget(self.canvas, 0, 1)
            elif index_father == 1:
                sip.delete(self.canvas)
                self.canvas = FigureCanvas(self.createPlot(self.retrieveTree(1)))
                self.gridlayout.addWidget(self.canvas, 0, 1)
    def retrieveTree(self,index):
        listOfTrees = [{'101': {0: '102', 1: {'node': {0: '103', 1: '104'}}}},
                    {'201': {0: '203', 1: {'node': {0: '203', 1: '204'}}}}
                ]
        return listOfTrees[index]
    def pictureView(self, inx):
        tree1 = self.retrieveTree(inx)
        self.horizontalLayout.addWidget(treePlotter.createPlot(tree1))
    def createPlot(self, inTree):
        fig = plt.figure()
        axprops = dict(xticks=[], yticks=[])
        treePlotter.createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
        treePlotter.plotTree.totalW = float(treePlotter.getNumLeafs(inTree))
        treePlotter.plotTree.totalD = float(treePlotter.getTreeDepth(inTree))
        treePlotter.plotTree.x0ff = -0.5 / treePlotter.plotTree.totalW
        treePlotter.plotTree.y0ff = 1.0
        treePlotter.plotTree(inTree, (0.5, 1.0), '')
        return fig
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui=myWindow()
    ui.show()
    sys.exit(app.exec_())