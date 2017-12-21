import 'dart:core';
import 'dart:io';

dynamic serve(int port) async {
  try {
    var server = await HttpServer.bind(InternetAddress.LOOPBACK_IP_V4, port);

    await for (HttpRequest request in server) {
      print("requested url: ${request.requestedUri.path}");

      File f = await new File("content${request.requestedUri.path}");

      request.uri.path.startsWith("//");
      request.response.headers.contentType = new ContentType("text", "html");

      request.response
        ..write(f.readAsStringSync())
        ..flush()
        ..close();
    }
  } catch (e) {
    print("exception raised");
  }
}

void main() {
  serve(9090);
}
