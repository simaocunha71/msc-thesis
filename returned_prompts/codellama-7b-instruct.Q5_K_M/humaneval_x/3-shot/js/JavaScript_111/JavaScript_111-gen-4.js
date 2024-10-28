  var hist = {};

  for (var i = 0; i < test.length; i++) {
    var cur_char = test[i];
    if (hist[cur_char] != undefined) {
      hist[cur_char] += 1;
    } else {
      hist[cur_char] = 1;
    }
  }

  return hist;
}



