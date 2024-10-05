  let words = txt.split(' ');
  if (words.length > 1) {
    return words;
  } else {
    let letters = words[0].split(',');
    if (letters.length > 1) {
      return letters;
    } else {
      let count = 0;
      for (let i = 0; i < words[0].length; i++) {
        if (words[0][i].toLowerCase() == words[0][i] && words[0][i].charCodeAt() % 2 == 1) {
          count += 1;
        }
      }
      return count;
    }
  }
}