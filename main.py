from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import *
import json
import os
import backup #import do modulo backup.py
import time

#Controller da ProgressBar
def progressBar(path):
    folder = os.listdir(path)
    files_list = []

    for files in folder:
        files_list.append(files)
        print(files)

    if 'desktop.ini' in files_list:
        files_list.remove('desktop.ini')

    count = len(files_list)

    return count

#Janela de Configuração
def config():
    file = open("config.json", "r")
    config_file = json.load(file)

    targetFolder = config_file["FolderTarget"]
    backupFolder = config_file["FolderBackup"]

    file.close()

    config_window.targetDisplay.setText(targetFolder)
    config_window.backupDisplay.setText(backupFolder)

    def targetFolder():
        pathTarget = QtWidgets.QFileDialog.getExistingDirectory()

        config_window.targetDisplay.setText(pathTarget)

        file = open("config.json", "r")
        config_file = json.load(file)

        config_file.update({"FolderTarget": pathTarget.replace("/", "\\")})
        file.close()

        file = open("config.json", "w")
        json.dump(config_file, file, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ":"))

    def backupFolder():
        pathBackup = QtWidgets.QFileDialog.getExistingDirectory()

        config_window.backupDisplay.setText(pathBackup)

        file = open("config.json", "r")
        config_file = json.load(file)

        config_file.update({"FolderBackup": pathBackup.replace("/", "\\") + "\\"})
        file.close()

        file = open("config.json", "w")
        json.dump(config_file, file, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ":"))

    def saveButton():
        config_window.close()

    config_window.selectTarget.clicked.connect(targetFolder)
    config_window.selectBakFolder.clicked.connect(backupFolder)
    config_window.save.clicked.connect(saveButton)
    config_window.show()

#Criação de Backup
def createBackup():
    file = open("config.json", "r")
    config_file = json.load(file)

    targetFolder = config_file["FolderTarget"]
    backupFolder = config_file["FolderBackup"]

    file.close()

    print(targetFolder)
    print(backupFolder)

    bak = backup.backupOptions(targetFolder, backupFolder)

    folder = os.listdir(targetFolder)
    files_list = []

    for files in folder:
        files_list.append(files)
        time.sleep(0.2)
        window.progressBar.setValue(len(files_list))
        print(files)

    if 'desktop.ini' in files_list:
        files_list.remove('desktop.ini')

    bak.RunBackup()

    window.progressBar.setValue(100)

# A ser utilizado em updates futuros
def automaticBackup():
    print("Backup2") #p


#Estrutura Básica
app = QtWidgets.QApplication([])
window = uic.loadUi("main.ui")
window.setWindowTitle("BackUps")
window.setWindowIcon(QIcon("assets/icon.png"))

window.config.clicked.connect(config)
window.runbackup.clicked.connect(createBackup)

config_window = uic.loadUi("config.ui")

window.show()
app.exec()