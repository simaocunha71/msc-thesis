  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    return txt.split('').filter(c => c >= 'a' && c <= 'z' && c.charCodeAt(0) % 2 == 1).length;
  }
}



