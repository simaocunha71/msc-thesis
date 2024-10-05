  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if ((txt[i].toLowerCase().charCodeAt(0) - 97) % 2 !== 0) {
        count++;
      }
    }
    return count;
  }
}...



