# Link Harvester JS
<img alt="JavaScript" src="https://img.shields.io/badge/javascript-%23323330.svg??style=flat&logo=appveyor&logoColor=%23F7DF1E" />
<a href="https://github.com/vltmedia/LinkHarvesterJS"><img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=flat&logo=github&logoColor=white" /></a>

# Description

Harvest links from the children of an element you specify on a webpage by using Xpath, which can be accessed through the inspect element function.

- User can receive a JSON or CSV file if needed.
- User can download a JSON or CSV with ```LinkHarvest_.DownloadJson()``` or ```LinkHarvest_.DownloadCSV()```



# Json Schema

```json
{
 url: "https://archive.org/download/Aru.zip",
 filename: "Aru.zip",
 extension: "zip",
 status: 0
}
```



# *Usage:*

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



# Functions

| Name              | Description                                              | Args           |
| ----------------- | -------------------------------------------------------- | -------------- |
| GetLinksFromXpath | Get the children ```<a href>``` from the Xpath provided  | xpath = string |
| DownloadJson      | Download Links document as Json file                     | -              |
| DownloadCSV       | Download Links document as CSV                           | -              |
| LinksToJson       | Get the Links as a JSON                                  | -              |
| LinksToCSV        | Get the Links as a CSV                                   | -              |
| GetURLExtension   | Get the Extension from the URL                           | url= string    |
| GetDateTime       | Get the current Date Time in a ```YMMDD_HHmmss``` format | -              |



# Variables

| Name      | Description                                                  | Args                                                         |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| links     | Array containing the current links in their url forms.       | -                                                            |
| linksjs   | Array containing the current links in their JSON object forms. | -                                                            |
| csvstring | If you ran ```LinksToCSV``` or ```DownloadCSV ``` this will contain the current CSV string representing the links. | -                                                            |
| csvheader | Change this if you want to change the CSV header output.     | default = ```LinkHarvester_.csvheader = "url,filename,extension,status";``` |

