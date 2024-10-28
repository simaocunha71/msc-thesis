  var lastChar = txt[txt.length - 1];
  var isLetter = /[a-zA-Z]/.test(lastChar);
  var isNotPartOfWord = txt[txt.length - 2] == ' ';
  return isLetter && isNotPartOfWord;
}



