  let result = [];
  if (txt.indexOf(' ') >= 0) {
    result = txt.split(' ');
  } else if (txt.indexOf(',') >= 0) {
    result = txt.split(',');
  } else {
    for (const c of txt) {
      if (c >= 'a' && c <= 'z') {
        if (c % 2 == 1) {
          result.push(c);
        }
      }
    }
    result = result.length;
  }
  return result;
}



