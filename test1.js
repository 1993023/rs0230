var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("ElementDb");
  dbo.createCollection("ElementCollec", function(err, res) 
  {
    if (err) throw err; 
    console.log("Collection created!");
    db.close();
  });


var TextBoxObj = { ElemName: "TextBox", datatype: "String" };
  dbo.collection("ElementCollec").insertOne(TextBoxObj, function(err, res) 
  {
    if (err) throw err;
    //console.log("Element inserted");
    db.close();
  });

var CheckBoxObj = { ElemName: "CheckBox", datatype: "Boolean" };
dbo.collection("ElementCollec").insertOne(CheckBoxObj, function(err, res) 
{
if (err) throw err;
//console.log("Element inserted");
db.close();
});

var radioButtonObj = { ElemName: "radioButton", datatype: "Boolean" };
dbo.collection("ElementCollec").insertOne(radioButtonObj, function(err, res) 
{
if (err) throw err;
//console.log("Element inserted");
db.close();
});


var spinBoxObj = { ElemName: "spinBox", datatype: "Number" };
dbo.collection("ElementCollec").insertOne(spinBoxObj, function(err, res) 
{
if (err) throw err;
//console.log("Element inserted");
db.close();
});


var comboBoxObj = { ElemName: "comboBox", datatype: "Boolean" };
dbo.collection("ElementCollec").insertOne(comboBoxObj, function(err, res) 
{
if (err) throw err;
//console.log("Element inserted");
db.close();
});



var dropDownButtonObj = { ElemName: "dropDownButton", datatype: "Boolean" };
dbo.collection("ElementCollec").insertOne(dropDownButtonObj, function(err, res) 
{
if (err) throw err;
//console.log("Element inserted");
db.close();
});


});

