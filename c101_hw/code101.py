import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))
def main():
    access_token = 'sl.BMBEA4zQfoKOnLmD9a0mARwNvODjSi39xV5G025-_30b8-ECdAWNTTAxbakFhCY4AtjfDtrlVcww-CfVIMDuI2hsWD-oBLxDaLE4LYRjI38i-u2UnLzcXG9rRp7PEwvRmFODhBI'
    transferData = TransferData(access_token)

    file_from = r'C:\Users\kobeh\Desktop\python\c101_hw\abc'
    file_to = '/kobehw101'

    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")

main()