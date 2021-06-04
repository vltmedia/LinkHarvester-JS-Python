# python LinkHarvest_ConvertIAList.py --input "C:\temp\psxdump.txt" --output "C:\temp\psxdump.json" --collection "Sony-Playstation-USA-Redump.org-2019-05-27"

import os
from classes import LinkObject
import urllib.parse
import json
from options import InternetArchiveOptions


class LinkHarvest_ConvertIAList:

    def __init__(self, filepath, outputpath, collectionpath):
        self.filepath = filepath
        self.outputpath = outputpath
        self.collectionpath = collectionpath
        self.LinkObjects = []
        self.IAUrl = 'https://archive.org/download/' + collectionpath + '/'
        self.opt = InternetArchiveOptions.InternetArchiveOptions().parse()
        

                
    def CreateLinkObject(self, url, filename, extension, status):
        LinkObject_ = LinkObject.LinkObject(url, filename,extension, status, self.opt)
        self.LinkObjects.append(LinkObject_)
    
    def WriteFile(self):
        if self.opt.exporttype == 'json':
            self.WriteJSONFile()
            
        if self.opt.exporttype == 'csv':
            self.WriteCSVFile()
            
        print('Successfully wrote file to : ', self.opt.output)
            
            
    def OpenFile(self):
        # Using readlines()
        file1 = open(self.filepath, 'r')
        Lines = file1.readlines()
        file1.close()
        self.outlines = []
        for line in Lines:
            cleanedline = line.strip()
            line = cleanedline
            if '(Demo)' not in line and 'Action Replay' not in line:
                
                urlencode = urllib.parse.quote(line.strip())
                baseurl = self.IAUrl + urlencode
                self.CreateLinkObject(baseurl, line, os.path.splitext(line)[1], 0)
        self.WriteFile()              
                
    # def CreateObject
    def WriteLinesToFile(self):
        # writing to file
        file1 = open(self.outputpath, 'w')
        file1.writelines(self.outlines)
        file1.close()
        
    def WriteJSONFile(self):
        outputjs = {"Links": []}
        for linkobj in self.LinkObjects:
            outjs = {"url": linkobj.url, "filename": linkobj.filename, "extension": linkobj.extension, "status": linkobj.status}
            outputjs['Links'].append(outjs)
        with open(self.opt.output, 'w') as outfile:
            json.dump(outputjs, outfile)
        outfile.close()
                
    def WriteCSVFile(self):
        outputcsv = "url,filename,extension,status\n"
        outputcsvarray = ["url,filename,extension,status"]
        for linkobj in self.LinkObjects:
            outstring = outputcsv + linkobj.url +","+ linkobj.filename.replace(',',"_") +","+linkobj.extension +","+str(linkobj.status) + "\n"
            outstring1 = linkobj.url +","+ linkobj.filename.replace(',',"_") +","+linkobj.extension +","+str(linkobj.status)
            outputcsvarray.append(outstring1)
            outputcsv = outstring
            
        with open(self.opt.output, 'w') as outfile:
            outfile.write(outputcsv)
        outfile.close()    


def main():
    options = InternetArchiveOptions.InternetArchiveOptions().parse()
    Links_ = LinkHarvest_ConvertIAList(options.input, options.output,options.collection )
    Links_.OpenFile()

if __name__ == '__main__':
    main()

