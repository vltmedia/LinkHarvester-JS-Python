import os
from demeter_dl.Core import HarvesterEngine


class LinkObject:
    '''Represents any school member.'''
    def __init__(self,url, filename, extnsion, status, options):
        self.url = url
        self.filename = filename
        self.extnsion = extnsion
        self.status = status
        self.outputpath = os.path.join(options.output, filename)
        self.CheckFileExists()
        self.opt = options
    
    def CheckFileExists(self):
        self.exists = os.path.exists(self.outputpath)
        if self.exists == True:
            self.status = 1
            print("Skipping | ", self.filename)
        else:
            self.status = 0
        
    def DownloadLink(self):
        download_instance = HarvesterEngine(self.url, file_name=self.filename, location=self.outputpath)  # This will use the custom options
        # print("Downloading Info | ", download_instance.Get_info())
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        
        print("Downloading Link | ", self.url)
        print("Please wait this may take a while...")
        download_instance.Download()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Finished! Link | ", self.url)
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
