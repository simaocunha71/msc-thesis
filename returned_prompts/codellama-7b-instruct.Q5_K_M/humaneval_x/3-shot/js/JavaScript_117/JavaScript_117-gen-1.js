  if (s.length == 0) {
    return [];
  }

  var words = s.split(' ');

  var result = [];

  for (var i = 0; i < words.length; i++) {
    var c = 0;
    for (var j = 0; j < words[i].length; j++) {
      var ch = words[i].charAt(j);
      if (ch != ' ') {
        c++;
      }
    }
    if (c == n) {
      result.push(words[i]);
    }
  }

  return result;
}



