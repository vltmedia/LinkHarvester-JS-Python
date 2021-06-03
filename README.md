# Link Harvester
<a href="https://github.com/vltmedia/LinkHarvesterJS"><img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=flat&logo=github&logoColor=white" /></a>
<img alt="JavaScript" src="https://img.shields.io/badge/javascript-%23323330.svg??style=flat&logo=appveyor&logoColor=%23F7DF1E" />
<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white"/>

# Description

Harvest links from the children of an element you specify on a webpage by using Xpath, which can be accessed through the inspect element function. This also contains a Python 3.5+ utility app to process and download the resulting links from the JSON and CSV files located in ```\py\LinkHarvest_Downloader.py```.

- User can receive a JSON or CSV file if needed.
- User can download a JSON or CSV with ```LinkHarvest_.DownloadJson()``` or ```LinkHarvest_.DownloadCSV()```
- User can download all the links in the resulting files with a Python 3.5+ app.  Example:  ```py/LinkeHarvest_Downloader.py --input C:/temp/LinksHarvested_2021-6-3_122311.json --output C:/temp/LinkHarvest --starting 0 --ending 5 ```.



# Json Schema

```json
{
 url: "https://archive.org/download/Aru.zip",
 filename: "Aru.zip",
 extension: "zip",
 status: 0
}
```

# Link Harvester JS

## Usage:

```javascript
var LinkHarvest_ = new LinkHarvest();
LinkHarvest_.GetLinksFromXpath('/html/body/div/main/div[5]/div/div/div[1]/div[6]/div[8]/div');

// Get the Links as a JSON
linkjson = LinkHarvest_.LinksToJson();
console.log(linkjson);

// Get the Links as a CSV
linkcsv = LinkHarvest_.LinksToCSV();
console.log(linkcsv);

// Download Links document as Json file 
LinkHarvest_.DownloadJson();

// Download Links document as CSV
LinkHarvest_.DownloadCSV();

```



## Functions

| Name              | Description                                              | Args           |
| ----------------- | -------------------------------------------------------- | -------------- |
| GetLinksFromXpath | Get the children ```<a href>``` from the Xpath provided  | xpath = string |
| DownloadJson      | Download Links document as Json file                     | -              |
| DownloadCSV       | Download Links document as CSV                           | -              |
| LinksToJson       | Get the Links as a JSON                                  | -              |
| LinksToCSV        | Get the Links as a CSV                                   | -              |
| GetURLExtension   | Get the Extension from the URL                           | url= string    |
| GetDateTime       | Get the current Date Time in a ```YMMDD_HHmmss``` format | -              |



## Variables

| Name      | Description                                                  | Args                                                         |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| links     | Array containing the current links in their url forms.       | -                                                            |
| linksjs   | Array containing the current links in their JSON object forms. | -                                                            |
| csvstring | If you ran ```LinksToCSV``` or ```DownloadCSV ``` this will contain the current CSV string representing the links. | -                                                            |
| csvheader | Change this if you want to change the CSV header output.     | default = ```LinkHarvester_.csvheader = "url,filename,extension,status";``` |

# Link Harvester Python
<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white"/>

A Python 3.5+ utility app to process and download the resulting links from the JSON and CSV files located in ```\py\LinkHarvest_Downloader.py```.

## Install

- Change directory to ```\py ``` .        ```cd \py```
- Run ```pip install -r requirements.txt``` or  ```pip3 install -r requirements.txt```

## CLI Usage:

```shell
LinkeHarvest_Downloader.py --input C:/temp/LinksHarvested_2021-6-3_122311.json --output C:/temp/LinkHarvest --starting 0 --ending 5 

LinkeHarvest_Downloader.py --input C:/temp/LinksHarvested_2021-6-3_122311.csv --output C:/temp/LinkHarvest --starting 0 --ending 5 

```

## Arguments

| Name            | Description                                                  | Example                                     |
| --------------- | ------------------------------------------------------------ | ------------------------------------------- |
| --input         | JSON, or CSV file to process. Created by the Link Harvester JS class above. | C:/temp/LinksHarvested_2021-6-3_122311.json |
| --output        | Directory to save the resulting downloaded files to.         | C:/temp/LinkHarvest                         |
| --starting      | The first index to download.                                 | 0                                           |
| --ending        | The last index to download.                                  | 10                                          |
| --searchstrings | comma sepearted strings to search for in the file names      | EN,USA                                      |

