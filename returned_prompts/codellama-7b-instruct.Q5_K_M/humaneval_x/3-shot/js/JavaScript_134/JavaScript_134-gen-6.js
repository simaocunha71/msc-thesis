  let lastChar = txt.charAt(txt.length-1);
  let lastCharIsLetter = lastChar.match(/[a-zA-Z]/);
  if (lastCharIsLetter) {
    let lastCharIsNotPartOfWord = !txt.endsWith(' ' + lastChar);
    return lastCharIsNotPartOfWord;
  } else {
    return false;
  }
}



