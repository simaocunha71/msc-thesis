  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    return txt.split('').filter(c => c == c.toLowerCase()).filter((c, i) => i % 2 == 1).length;
  }
}