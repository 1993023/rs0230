var express = require("express");
var app = express();
var port = 3000;
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

var mongoose = require("mongoose");
mongoose.Promise = global.Promise;
mongoose.connect("mongodb://localhost:27017/TestElement",{ useNewUrlParser: true });

var ElemSchemma = new mongoose.Schema({
    TextBox: {
         type: String },
    
    CheckBox: {
        type:Array },
    
    RadioButton: {
        type: String },
    
    SpinBox: {
        type:String },
    
    comboBox: {
        type: Array },
        
    
    dropDownButton: {
        type: String },

},
 {
	collection: 'TestElemeCollec'
});

// var oldSchema = new mongoose.Schema({
//     firstName: String,
//     lastName: String,
//     address:String,
//     phone:String,
//     Email:String

// },
//  {
// 	collection: 'TestCollec'
// });


var User = mongoose.model("User", ElemSchemma);
app.get("/", (req, res) => {
    res.sendFile("/home/rahul/formJs/Elements/index.html");
});

app.post("/addname", (req, res) => {
    var myData = new User(req.body);
    myData.save()
        .then(item => {
            res.send("Name saved to database");
        })
        .catch(err => {
            res.status(400).send("Unable to save to database");
        });
});

app.listen(port, () => {
    console.log("Server listening on port " + port);
});
