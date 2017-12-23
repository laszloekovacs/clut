
import 'dart:io';
import 'dart:convert';





void main () {

  var utf8_codec = new Utf8Codec();
  var gzip_codec = new GZipCodec();

  List<int> data = gzip_codec.encode(utf8_codec.encode("hello from dart! compress this"));

  for (var code in data) {
    print(code.toString());
  }

  String orig = utf8_codec.decode(gzip_codec.decode(data));

  print(orig);
}