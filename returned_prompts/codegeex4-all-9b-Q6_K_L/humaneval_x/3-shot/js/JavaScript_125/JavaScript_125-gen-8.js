  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    let count = 0;
    for (const c of txt) {
      if (c.toLowerCase() != c.toUpperCase()) {
        count += 1;
      }
    }
    return count;
  }
}