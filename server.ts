
import * as http from "http";
import * as os from "os";
import { print } from "util";



function main() : void {
    console.log("the free memory is:" + String(Math.floor(os.freemem() / (1024 * 1024))) + " MB");

    let server = http.createServer((req, res) => {

        res.end();
    });
    
    server.listen(9090);

    server.addListener("connection", () => {
        console.log("someone just logged in");
    });
}

let pattern = 'barry/options/main//garry'.split("/");
console.log(pattern);


main();