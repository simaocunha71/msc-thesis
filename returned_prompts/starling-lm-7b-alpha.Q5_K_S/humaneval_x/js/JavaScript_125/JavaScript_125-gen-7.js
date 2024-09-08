  let result = [];
  if (txt.includes(' ')) {
    result = txt.split(' ');
  } else if (txt.includes(',')) {
    result = txt.split(',');
  } else {
    let counter = 0;
    for (const c of txt) {
      if (c.toLowerCase() == c && (ord(c) % 2) == 1) {
        counter += 1;
      }
    }
    result = counter;
  }

  return result;
}



