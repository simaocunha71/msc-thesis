  let words = [];
  let count = 0;
  let c;
  for (let i = 0; i < txt.length; i++) {
    c = txt[i];
    if (c == ' ' || c == ',' || c == '!') {
      words.push(txt.slice(count, i));
      count = i + 1;
    }
    if (c >= 'a' && c <= 'z') {
      if (count % 2 == 1) {
        count += 1;
      } else {
        count -= 1;
      }
    }
  }
  if (count != txt.length) {
    words.push(txt.slice(count));
  }
  if (words.length == 0) {
    return txt.length;
  }
  return words;
}



