import zipfile
import datetime
import os

class backupOptions():

    def __init__(self, target, backup):
        self.folder_target = target
        self.pathbackup = backup

    def RunBackup(self):

        #Data atual
        date_now = str(datetime.date.today())

        folder_target = self.folder_target #Pasta alvo para backup
        pathbackup = self.pathbackup + date_now + ".zip" #Caminho da pasta de bakcup

        backup_zip = zipfile.ZipFile(pathbackup, 'w') #Criação do arquivo .zip

        for folder, subfolders, files in os.walk(folder_target):
            for file in files:
                backup_zip.write(os.path.join(folder, file),
                                  os.path.relpath(os.path.join(folder, file), folder_target),
                                  compress_type=zipfile.ZIP_DEFLATED)

        backup_zip.close()



    def AutomaticBackup(self, date):

        if date == 6:
            self.RunBackup()