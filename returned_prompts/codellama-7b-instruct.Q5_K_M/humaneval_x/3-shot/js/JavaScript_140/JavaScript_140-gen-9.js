  var result = '';
  var temp = '';
  var count = 0;
  
  for (const c of text) {
    if (c == ' ') {
      if (count > 1) {
        result += '-';
        count = 0;
      } else {
        result += '_';
        count += 1;
      }
    } else {
      result += c;
      count = 0;
    }
  }
  
  return result;
}



