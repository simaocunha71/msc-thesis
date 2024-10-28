  let words = txt.split(' ');
  if (words.length == 1) {
    words = txt.replace(/[^a-z]/g, '').split(',');
    if (words.length == 1) {
      return words[0].toLowerCase().split('').filter((c, i) => i % 2 == 1).length;
    } else {
      return words;
    }
  } else {
    return words;
  }
}...



