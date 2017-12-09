"use strict";
exports.__esModule = true;
var http = require("http");
var os = require("os");
function main() {
    console.log("the free memory is:" + String(Math.floor(os.freemem() / (1024 * 1024))) + " MB");
    var server = http.createServer(function (req, res) {
        res.end();
    });
    server.listen(9090);
    server.addListener("connection", function () {
        console.log("someone just logged in");
    });
}
var pattern = 'barry/options/main//garry'.split("/");
console.log(pattern);
main();
