  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    let count = 0;
    for (const c of txt) {
      if (c.toLowerCase() != c) {
        count += 1;
      }
    }
    return count;
  }
}



