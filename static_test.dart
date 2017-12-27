import 'dart:core';
import 'dart:io';

String contentpath = "content";

// the domain is registered as dev.local.com

void serveStatic(HttpRequest request) {

  print(request.requestedUri.toString());

  
  // try to open the static file
  File file = new File(contentpath + request.uri.toFilePath());

  //read file into the response
  request.response.write(file.readAsStringSync());
  //flush and close the response
  request.response.flush().then((_) => request.response.close());
}


void main() {
  
  

  HttpServer.bind(InternetAddress.ANY_IP_V4, 8080)
  .then((server) {
    print("bound and ready");
    server.listen(serveStatic);
  });

}