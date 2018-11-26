var express = require("express");
var app = express();
var port = 3000;
var fs = require('fs');
var ObjectId = require('mongodb').ObjectID
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));


var mongoose = require("mongoose");
mongoose.Promise = global.Promise;
uri=mongoose.connect("mongodb://localhost:27017/DynamicDb",{ useNewUrlParser: true });

var TextBoxids=[]

var assert = require('assert')

// get reference to database
var db = mongoose.connection; 

db.once('open', function() {
    console.log("Connection Successful!");
})

//TextBoxId=db.collection("savedatas").save({"_id" : ObjectId('5bf7a23b639b210f7a4f1c59'),elem:"TextBox"})


var ElementSchema = new mongoose.Schema({
        // id:{type:String},
        // Txb01 : {type: String},
        // Txb02 : {type: String},
        "ObjectId('5bf7a23b639b210f7a4f1c59')":{type:String},
       

    // CheckBox:{
        "ObjectId('5bf7a23b639b210f7a4f1c5a')":{type: String},
    

    // RadioButton
        "ObjectId('5bf7a23b639b210f7a4f1c5b')":{type:String},

    
    //SpinBox
        "ObjectId('5bf7a23b639b210f7a4f1c5c')":{type:String},
       
       
    // comboBox:{
        "ObjectId('5bf7a23b639b210f7a4f1c5d')":{type:String},
    

    // dropDownButton:{
       "ObjectId('5bf7a23b639b210f7a4f1c5e')":{type:String},

   
    
});

var SaveData = mongoose.model('SaveData', ElementSchema);

app.get("/", (req, res) => {
    res.sendFile("/home/rahulkumar/formJs/Elements/index2.html");

});

app.post("/feelup", (req, res) => {
    var myData = new SaveData(req.body);
    //console.log(req.body)
    myData.save()
    
        .then(item => {
            res.send("saved in database");
        })
        .catch(err => {
            res.status(400).send("error not save in database");
        });
        fs.appendFile('/home/rahulkumar/Form.txt', myData, function(err, data){
            if (err) console.log(err);
            console.log("Successfully Written to File.");
        });
});

app.listen(port, () => {
    console.log("Server listening on port " + port);
});
