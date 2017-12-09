import 'dart:core';
import 'dart:io';


void maintainednolonger(dynamic) {
  return;
}

void main () {

  var v = Platform.numberOfProcessors;

  print('number of cpus:' + v.toString());
}
