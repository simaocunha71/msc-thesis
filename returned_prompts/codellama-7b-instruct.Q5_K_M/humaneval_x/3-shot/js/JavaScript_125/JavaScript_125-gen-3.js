  var result = [];
  var temp = '';

  for (const c of txt) {
    if (c == ' ' || c == ',') {
      if (temp != '') {
        result.push(temp);
        temp = '';
      }
    } else {
      temp += c;
    }
  }

  if (temp != '') {
    result.push(temp);
  }

  if (result.length == 0) {
    var total = 0;
    for (var i = 0; i < txt.length; i++) {
      if (txt[i] >= 'a' && txt[i] <= 'z') {
        total += i % 2;
      }
    }
    return total;
  } else {
    return result;
  }
}



