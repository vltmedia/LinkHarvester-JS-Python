# LinkeHarvest_Downloader.py --input C:/temp/thing.csv --output C:/temp/out --downloadcount 2
# LinkeHarvest_Downloader.py --input C:/temp/LinksHarvested_2021-6-3_122311.csv --output C:/temp/LinkHarvest --downloadcount 2
# LinkeHarvest_Downloader.py --input C:/temp/LinksHarvested_2021-6-3_122311.json --output C:/temp/LinkHarvest --starting 0 --ending 5 --downloadcount 2

from demeter_dl.Core import HarvesterEngine

from classes import LinkObject
from options import BaseOptions
from util import util
import os
import csv
import json

class LinkHarvester_DownloadManager:

    # instance attribute
    def __init__(self):
        self.CSVArray = []
        self.JSONObject = {"Links":[]} 
        self.LinkObjects = []
        
        self.opt = BaseOptions.BaseOptions().parse()
        self.CheckIfOutputExists()
        self.GetFileType()
        self.ReadInfile()
        self.ProcessLinkArray()
        
        
    def CheckIfOutputExists(self):
        if not os.path.exists(self.opt.output):
            os.mkdir(self.opt.output)
            print("Created Output Directory : ", self.opt.output)
    
    def CSVArrayToLinksArray(self):
        self.LinkObjects = []
        for row in self.CSVArray:
            LinkObject_ = LinkObject.LinkObject(row[0], row[1],row[2], row[3], self.opt)
            self.LinkObjects.append(LinkObject_)
        
    def JSONObjectToLinksArray(self):
        self.LinkObjects = []
        for row in self.JSONObject['Links']:
            LinkObject_ = LinkObject.LinkObject(row['url'], row['filename'],row['extension'], row['status'], self.opt)
            self.LinkObjects.append(LinkObject_)
        
        
    def ReadInfile(self):
        if os.path.exists(self.opt.input):
            
            if self.Filetype == 'csv':
                file = open(self.opt.input,"r+")
                reader = csv.reader(file)
                for row in reader:
                    self.CSVArray.append(row)
                
                file.close()
                self.CSVArray.pop(0)
                self.CSVArrayToLinksArray()
                
            
            
            if self.Filetype == 'json':
                with open(self.opt.input) as f:
                    self.JSONObject = json.load(f)
                    f.close()
                # print(self.JSONObject['Links'][0])
                self.JSONObjectToLinksArray()
            
            

        else:
            print('Input file does not exist!')
    
    def GetFileType(self):
        if 'json' in self.opt.input:
            self.Filetype = 'json'
        if 'csv' in self.opt.input:
            self.Filetype = 'csv'

    def GetFileInfo(self, url):
        download_instance = HarvesterEngine(url)  # This will use the default options
        print(download_instance.Get_info())
        
    
    def ProcessLinkArray(self):
        endingIndex = self.opt.ending
        if endingIndex == 9999:
            endingIndex = len(self.LinkObjects) - 1
        for indexx in range(self.opt.starting , endingIndex):
            
            # Start Processing here!
            # -----------------------------------------------
            # -----------------------------------------------
            print("Downloading "+str(indexx + 1)+" of "+str(endingIndex ))
            self.LinkObjects[indexx].DownloadLink()
            # self.GetFileInfo(self.LinkObjects[indexx].url)
            
            
            # -----------------------------------------------
            # -----------------------------------------------
    
            
            
        
def main():
    LinkHarvester_DownloadManager_ = LinkHarvester_DownloadManager()
    

if __name__ == '__main__':
    main()