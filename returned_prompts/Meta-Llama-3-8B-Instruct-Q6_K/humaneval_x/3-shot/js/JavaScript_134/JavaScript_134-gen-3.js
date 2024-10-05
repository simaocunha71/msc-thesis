  let lastChar = txt.slice(-1);
  let lastCharIsLetter = lastChar.match(/[a-zA-Z]/);
  let lastCharIsPartOfWord = txt.match(/ [a-zA-Z]$/);

  return lastCharIsLetter && !lastCharIsPartOfWord;
}