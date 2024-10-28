  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    let result = 0;
    for (const c of txt) {
      if (c >= 'a' && c <= 'z') {
        if ((c.charCodeAt(0) - 'a'.charCodeAt(0)) % 2 == 1) {
          result += 1;
        }
      }
    }
    return result;
  }
}