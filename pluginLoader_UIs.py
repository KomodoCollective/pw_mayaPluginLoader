# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dropbox\Dropbox\pw_prefs\RnD\maya\python\OTHER\pluginLoader\pluginLoader.ui'
#
# Created: Mon Feb 16 11:44:27 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_pluginLoader(object):
    def setupUi(self, pluginLoader):
        pluginLoader.setObjectName("pluginLoader")
        pluginLoader.resize(416, 388)
        self.centralwidget = QtGui.QWidget(pluginLoader)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pluginPath_led = QtGui.QLineEdit(self.groupBox)
        self.pluginPath_led.setObjectName("pluginPath_led")
        self.horizontalLayout.addWidget(self.pluginPath_led)
        self.pluginInfo_btn = QtGui.QPushButton(self.groupBox)
        self.pluginInfo_btn.setMinimumSize(QtCore.QSize(40, 0))
        self.pluginInfo_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pluginInfo_btn.setObjectName("pluginInfo_btn")
        self.horizontalLayout.addWidget(self.pluginInfo_btn)
        self.pluginBrowse_btn = QtGui.QPushButton(self.groupBox)
        self.pluginBrowse_btn.setMinimumSize(QtCore.QSize(40, 0))
        self.pluginBrowse_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pluginBrowse_btn.setObjectName("pluginBrowse_btn")
        self.horizontalLayout.addWidget(self.pluginBrowse_btn)
        self.pluginRemove_btn = QtGui.QPushButton(self.groupBox)
        self.pluginRemove_btn.setMinimumSize(QtCore.QSize(40, 0))
        self.pluginRemove_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pluginRemove_btn.setObjectName("pluginRemove_btn")
        self.horizontalLayout.addWidget(self.pluginRemove_btn)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loadScene_cbx = QtGui.QCheckBox(self.groupBox_2)
        self.loadScene_cbx.setText("")
        self.loadScene_cbx.setChecked(True)
        self.loadScene_cbx.setObjectName("loadScene_cbx")
        self.horizontalLayout_2.addWidget(self.loadScene_cbx)
        self.scenePath_led = QtGui.QLineEdit(self.groupBox_2)
        self.scenePath_led.setObjectName("scenePath_led")
        self.horizontalLayout_2.addWidget(self.scenePath_led)
        self.setCurrentScene_btn = QtGui.QPushButton(self.groupBox_2)
        self.setCurrentScene_btn.setMinimumSize(QtCore.QSize(40, 0))
        self.setCurrentScene_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.setCurrentScene_btn.setObjectName("setCurrentScene_btn")
        self.horizontalLayout_2.addWidget(self.setCurrentScene_btn)
        self.sceneBrowse_btn = QtGui.QPushButton(self.groupBox_2)
        self.sceneBrowse_btn.setMinimumSize(QtCore.QSize(40, 0))
        self.sceneBrowse_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.sceneBrowse_btn.setObjectName("sceneBrowse_btn")
        self.horizontalLayout_2.addWidget(self.sceneBrowse_btn)
        self.sceneremove_btn = QtGui.QPushButton(self.groupBox_2)
        self.sceneremove_btn.setMinimumSize(QtCore.QSize(40, 0))
        self.sceneremove_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.sceneremove_btn.setObjectName("sceneremove_btn")
        self.horizontalLayout_2.addWidget(self.sceneremove_btn)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scriptEditor_ly = QtGui.QVBoxLayout()
        self.scriptEditor_ly.setSpacing(0)
        self.scriptEditor_ly.setObjectName("scriptEditor_ly")
        self.horizontalLayout_3.addLayout(self.scriptEditor_ly)
        self.eval_btn = QtGui.QPushButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eval_btn.sizePolicy().hasHeightForWidth())
        self.eval_btn.setSizePolicy(sizePolicy)
        self.eval_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.eval_btn.setObjectName("eval_btn")
        self.horizontalLayout_3.addWidget(self.eval_btn)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.gridLayout.setObjectName("gridLayout")
        self.load_btn = QtGui.QPushButton(self.centralwidget)
        self.load_btn.setObjectName("load_btn")
        self.gridLayout.addWidget(self.load_btn, 0, 0, 1, 1)
        self.reload_btn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reload_btn.sizePolicy().hasHeightForWidth())
        self.reload_btn.setSizePolicy(sizePolicy)
        self.reload_btn.setObjectName("reload_btn")
        self.gridLayout.addWidget(self.reload_btn, 0, 1, 2, 1)
        self.unload_btn = QtGui.QPushButton(self.centralwidget)
        self.unload_btn.setObjectName("unload_btn")
        self.gridLayout.addWidget(self.unload_btn, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        pluginLoader.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(pluginLoader)
        self.statusbar.setObjectName("statusbar")
        pluginLoader.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(pluginLoader)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 416, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        pluginLoader.setMenuBar(self.menuBar)
        self.openSettings_act = QtGui.QAction(pluginLoader)
        self.openSettings_act.setObjectName("openSettings_act")
        self.quit_act = QtGui.QAction(pluginLoader)
        self.quit_act.setObjectName("quit_act")
        self.actionClear_settings = QtGui.QAction(pluginLoader)
        self.actionClear_settings.setObjectName("actionClear_settings")
        self.menuFile.addAction(self.openSettings_act)
        self.menuFile.addAction(self.quit_act)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(pluginLoader)
        QtCore.QMetaObject.connectSlotsByName(pluginLoader)

    def retranslateUi(self, pluginLoader):
        pluginLoader.setWindowTitle(QtGui.QApplication.translate("pluginLoader", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("pluginLoader", "Plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.pluginInfo_btn.setText(QtGui.QApplication.translate("pluginLoader", "inf", None, QtGui.QApplication.UnicodeUTF8))
        self.pluginBrowse_btn.setText(QtGui.QApplication.translate("pluginLoader", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pluginRemove_btn.setText(QtGui.QApplication.translate("pluginLoader", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("pluginLoader", "Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.setCurrentScene_btn.setText(QtGui.QApplication.translate("pluginLoader", "Curr", None, QtGui.QApplication.UnicodeUTF8))
        self.sceneBrowse_btn.setText(QtGui.QApplication.translate("pluginLoader", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.sceneremove_btn.setText(QtGui.QApplication.translate("pluginLoader", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("pluginLoader", "Script", None, QtGui.QApplication.UnicodeUTF8))
        self.eval_btn.setText(QtGui.QApplication.translate("pluginLoader", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.load_btn.setText(QtGui.QApplication.translate("pluginLoader", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.reload_btn.setText(QtGui.QApplication.translate("pluginLoader", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.unload_btn.setText(QtGui.QApplication.translate("pluginLoader", "Unload", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("pluginLoader", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.openSettings_act.setText(QtGui.QApplication.translate("pluginLoader", "Open settings file", None, QtGui.QApplication.UnicodeUTF8))
        self.quit_act.setText(QtGui.QApplication.translate("pluginLoader", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_settings.setText(QtGui.QApplication.translate("pluginLoader", "Clear settings", None, QtGui.QApplication.UnicodeUTF8))

