  var distinctCharacters = new Set();

  for  (let i = 0; i < string.length; i++) {
    let lowerCaseChar = string[i].toLowerCase();
    distinctCharacters.add(lowerCaseChar);
  }

  return distinctCharacters.size;
}



