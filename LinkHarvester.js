// Harvest links from the children of an element you specify by Xpath. User can recieve a JSON or CSV file if needed.

// // Json Schema:
// {url: "https://archive.org/download/co%20Aru%20Koto%20wa%20Sando%20R%20%28Japan%29.zip", filename: "2do_Aru_Koto_wa_Sando_R_(Japan).zip", extension: "zip", status: 0}

// // Usage:
// var LinkHarvest_ = new LinkHarvest()
// LinkHarvest_.GetLinksFromXpath('/html/body/div/main/div[5]/div/div/div[1]/div[6]/div[8]/div')
// linkjson = LinkHarvest_.LinksToJson();


class LinkHarvest{

    constructor() {
        this.links = [];
        this.linksjs = {"Links":[]};
        this.GetLinksFromXpath = this.GetLinksFromXpath.bind(this);
        this.LinksToJson = this.LinksToJson.bind(this);
        this.LinksToCSV = this.LinksToCSV.bind(this);
        this.GetURLExtension = this.GetURLExtension.bind(this);
        this.GetDateTime = this.GetDateTime.bind(this);
        this.DownloadJson = this.DownloadJson.bind(this);
        this.DownloadCSV = this.DownloadCSV.bind(this);
        this.csvheader = "url,filename,extension,status";
        this.csvstring = this.csvheader + '\n';
    }

GetLinksFromXpath(xpath){
var basee = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

var linkss = basee.getElementsByTagName('a');
this.links =  linkss;
}

GetUrlBaseName(url){
    var parsed = decodeURI(url);
    return parsed.substring(parsed.lastIndexOf('/')+1).replaceAll(" ", "_");

}

GetURLExtension(url){

    var parsed = decodeURI(url);
    var ext = parsed.substr(parsed.lastIndexOf('.') + 1);
    return ext;

}

LinksToJson(){
    this.linksjs.Links = [];
for(var i =0; i < this.links.length - 1; i ++){
    var currentlink = this.links[i].href;
    var jsobject = {"url":currentlink, "filename":this.GetUrlBaseName(currentlink), "extension":this.GetURLExtension(currentlink), "status": 0};
    this.linksjs.Links.push(jsobject);

}

return this.linksjs;
}


LinksToCSV(){
this.csvstring = this.csvheader  + '\n';
for(var i =0; i < this.links.length - 1; i ++){
    var currentlink = this.links[i].href;
    var csvrow = currentlink+","+this.GetUrlBaseName(currentlink)+","+this.GetURLExtension(currentlink)+",0\n";
    var addedrow = this.csvstring + csvrow;
    this.csvstring  = addedrow;

}

return this.csvstring;
}

GetDateTime(){
    var today = new Date();
var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
var time = today.getHours() + "" + today.getMinutes() + "" + today.getSeconds();
var dateTime = date+'_'+time;
return dateTime;
}

DownloadJson(){
    this.LinksToJson();
    var fileContent = JSON.stringify( this.linksjs,2);
var fileName = 'LinksHarvested_'+this.GetDateTime()+'.json';
const blob = new Blob([fileContent], { type: 'text/plain' });
const a = document.createElement('a');
a.setAttribute('download', fileName);
a.setAttribute('href', window.URL.createObjectURL(blob));
a.click();
}

DownloadCSV(){
    this.LinksToCSV();
    var fileContent = this.csvstring;
var fileName = 'LinksHarvested_'+this.GetDateTime()+'.csv';
const blob = new Blob([fileContent], { type: 'text/plain' });
const a = document.createElement('a');
a.setAttribute('download', fileName);
a.setAttribute('href', window.URL.createObjectURL(blob));
a.click();
}

}



// ---------------------------------------------------------------------
// ---------------------------------------------------------------------
// ---------------------------------------------------------------------

// Example Stuff Starts Here ::

// var LinkHarvest_ = new LinkHarvest();
// LinkHarvest_.GetLinksFromXpath('/html/body/div/main/div[5]/div/div/div[1]/div[6]/div[8]/div');
// linkjson = LinkHarvest_.LinksToJson();
// console.log(linkjson);

// // Get the Links as a JSON
// linkjson = LinkHarvest_.LinksToJson();
// console.log(linkjson);

// // Get the Links as a CSV
// linkcsv = LinkHarvest_.LinksToCSV();
// console.log(linkcsv);

// // Download Links document as Json file 
// LinkHarvest_.DownloadJson();

// // Download Links document as CSV
// LinkHarvest_.DownloadCSV();

// Example Stuff Ends Here ::

// ---------------------------------------------------------------------
// ---------------------------------------------------------------------
// ---------------------------------------------------------------------
