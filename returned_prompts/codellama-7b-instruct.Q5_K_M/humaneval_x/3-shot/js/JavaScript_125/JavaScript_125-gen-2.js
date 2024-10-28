  var result = [];

  if (txt.includes(' ')) {
    result = txt.split(' ');
  } else if (txt.includes(',')) {
    result = txt.split(',');
  } else {
    var count = 0;
    for (var i = 0; i < txt.length; i++) {
      if (txt[i].charCodeAt(0) % 2 == 1) {
        count += 1;
      }
    }
    result.push(count);
  }

  return result;
}



