  let lastChar = txt.slice(-1).toLowerCase();
  let lastCharIndex = txt.lastIndexOf(lastChar);
  let lastCharIsPartOfWord = lastCharIndex > 0 && txt[lastCharIndex - 1] !== ' ';
  return lastChar.match(/[a-z]/) !== null && !lastCharIsPartOfWord;
}