  var result = [];

  if (txt.indexOf(' ') > -1) {
    result = txt.split(' ');
  } else if (txt.indexOf(',') > -1) {
    result = txt.split(',');
  } else {
    var count = 0;
    for (var i = 0; i < txt.length; i++) {
      var c = txt.charCodeAt(i);
      if (c >= 97 && c <= 122) {
        if (i % 2 != 0) {
          count++;
        }
      }
    }
    result = count;
  }

  return result;
}



