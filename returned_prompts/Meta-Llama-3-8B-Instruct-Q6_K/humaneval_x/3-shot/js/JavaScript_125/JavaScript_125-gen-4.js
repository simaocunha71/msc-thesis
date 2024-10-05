  let words = txt.replace(/ /g, ',').split(',');
  if (words.length === 1) {
    let sum = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt[i].toLowerCase() >= 'a' && txt[i].toLowerCase() <= 'z') {
        sum += parseInt(txt[i].toLowerCase().charCodeAt(0) - 97) % 2 === 1;
      }
    }
    return sum;
  } else {
    return words;
  }
}