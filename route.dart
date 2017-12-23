import 'dart:core';
import 'dart:async';
import 'dart:io';

Stream<int> getthings() async* {
  while (true) {
    sleep(new Duration(seconds: 1));
    yield 66;
  }
}

Future main() async {
  Stopwatch perf = new Stopwatch();
  perf.start();
  Stream m = getthings().asBroadcastStream();
  perf.stop();

  print("spent ${perf.elapsedMilliseconds} ms");

  m.listen((data) {
    print("listening to ${data}");
  });

  m.listen((data) {
    print("also listening: ${data}");
  });
}
