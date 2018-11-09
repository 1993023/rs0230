// var express = require("express");
// var app = express();
// var port = 3000;
// var bodyParser = require('body-parser');
// app.use(bodyParser.json());
// app.use(bodyParser.urlencoded({ extended: true }));

// var mongoose = require("mongoose");
// mongoose.Promise = global.Promise;
// mongoose.connect("mongodb://localhost:27017/Elements",{ useNewUrlParser: true });

// var ElemSchemma = new mongoose.Schema({
//     firstName: String,
   

// },
//  {
// 	collection: 'ElementsCollec'
// });
// var User = mongoose.model("User", ElemSchemma);
// app.get("/", (req, res) => {
//     res.sendFile("/home/rahul/formJs/nodefst/src/index.html");
// });

// app.post("/addname", (req, res) => {
//     var myData = new User(req.body);
//     myData.save()
//         .then(item => {
//             res.send("Name saved to database");
//         })
//         .catch(err => {
//             res.status(400).send("Unable to save to database");
//         });
// });

// app.listen(port, () => {
//     console.log("Server listening on port " + port);
// });


// ###########################  testing with mongodb ###########

// const MongoClient = require('mongodb').MongoClient;
// const assert = require('assert');
 
// // Connection URL
// const url = 'mongodb://localhost:27017';
 
// // Database Name
// const dbName = 'ElementDb';
 
// // Use connect method to connect to the server
// MongoClient.connect(url, function(err, client) {
//   assert.equal(null, err);
//   console.log("Connected successfully to server");
 
//   const db = client.db(dbName);
 
//   client.close();
// });

// ########################## insert into coolection ################

// var MongoClient = require('mongodb').MongoClient;
// var url = "mongodb://localhost:27017/";

// MongoClient.connect(url, function(err, db) {
//   if (err) throw err;
//   var dbo = db.db("mydb");
//   var myobj = { name: "Company Inc", address: "Highway 37" };
//   dbo.collection("customers").insertOne(myobj, function(err, res) 
//   {
//     if (err) throw err;
//     console.log("1 document inserted");
//     db.close();
//   });
// }); 






