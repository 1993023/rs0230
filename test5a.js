var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("DynamicDb");
  dbo.createCollection("ElementNameCollec", function(err, res) 
  {
    if (err) throw err; 
    console.log("Collection created!");
    db.close();
  });


var TextBoxObj = { ElemName: "TextBox", datatype: "String" };
  dbo.collection("ElementNameCollec").insertOne(TextBoxObj, function(err, res) 
  {
    if (err) throw err;
    //console.log("Element inserted");
    db.close();
  });

var CheckBoxObj = { ElemName: "CheckBox", datatype: "Array" };
dbo.collection("ElementNameCollec").insertOne(CheckBoxObj, function(err, res) 
{
if (err) throw err;
//console.log("Element inserted");
db.close();
});

var radioButtonObj = { ElemName: "radioButton", datatype: "String" };
dbo.collection("ElementNameCollec").insertOne(radioButtonObj, function(err, res) 
{
if (err) throw err;
//console.log("Element inserted");
db.close();
});


var spinBoxObj = { ElemName: "spinBox", datatype: "String" };
dbo.collection("ElementNameCollec").insertOne(spinBoxObj, function(err, res) 
{
if (err) throw err;
//console.log("Element inserted");
db.close();
});


var comboBoxObj = { ElemName: "comboBox", datatype: "Array" };
dbo.collection("ElementNameCollec").insertOne(comboBoxObj, function(err, res) 
{
if (err) throw err;
//console.log("Element inserted");
db.close();
});


var dropDownButtonObj = { ElemName: "dropDownButton", datatype: "String" };
dbo.collection("ElementNameCollec").insertOne(dropDownButtonObj, function(err, res) 
{
if (err) throw err;
//console.log("Element inserted");
db.close();
});


});

