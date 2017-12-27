
import 'dart:core';
import 'package:test/test.dart';

void main([List<String> args]) {
  
  test('check something very simple', () {
    int val = 7;
    String msg = "Value is $val";
  
    expect(msg, equals("Value is 8"));
  });
}