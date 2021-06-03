import os
from demeter_dl.Core import HarvesterEngine


class LinkObject:
    '''Represents any school member.'''
    def __init__(self,url, filename, extension, status, options):
        self.url = url
        self.filename = filename
        self.extension = extension
        self.status = status
        self.outputpath = os.path.join(options.output, filename)
        self.opt = options
        
        self.CheckToSkipBasedOnName()
        self.CheckFileExists()
    
    def CheckToSkipBasedOnName(self):
        shoulduse = False
        if ',' in self.opt.searchstrings:
            splitt = self.opt.searchstrings.split(',')
            for stringg in splitt:
                if stringg in self.filename:
                    shoulduse = True
        else:
            if self.opt.searchstrings in self.filename:
                shoulduse = True
            
        if shoulduse == False:
            self.status = 1
                    
                
    def CheckFileExists(self):
        self.exists = os.path.exists(self.outputpath)
        if self.exists == True:
            self.status = 1
            print("Skipping | ", self.filename)
        else:
            self.status = 0
        
    def DownloadLink(self):
        if self.status == 0:
            download_instance = HarvesterEngine(self.url, file_name=self.filename, location=self.outputpath)  # This will use the custom options
            # print("Downloading Info | ", download_instance.Get_info())
            print("----------------------------------------------------------")
            print("----------------------------------------------------------")
            
            print("Downloading Link | ", self.url)
            print("Please wait this may take a while...")
            download_instance.Download()
            self.status = 1;
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Finished! Link | ", self.url)
            print("----------------------------------------------------------")
            print("----------------------------------------------------------")
        else:
            print("----------------------------------------------------------")
            print("----------------------------------------------------------")
            print("Skipping File! : ", self.filename)
            
            print("----------------------------------------------------------")
            print("----------------------------------------------------------")