  let words = txt.split(' ');
  if (words.length == 1 && words[0].indexOf(',') != -1) {
    words = words[0].split(',');
  }
  if (words.length == 1) {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt[i].toLowerCase() >= 'a' && txt[i].toLowerCase() <= 'z' && (i % 2) == 1) {
        count++;
      }
    }
    return count;
  }
  return words;
}...



