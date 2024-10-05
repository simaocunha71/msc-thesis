  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    return txt.split('').filter(c => c == c.toLowerCase()).filter(c => (c.charCodeAt(0) - 'a'.charCodeAt(0)) % 2 == 1).length;
  }
}