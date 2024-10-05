
function findMax(listOfWords) {
  let maxUniqueCharacters = 0;
  let wordWithMaxUniqueCharacters;
  for (let i = 0; i < listOfWords.length; i++) {
    const currentWord = listOfWords[i];
    if (currentWord.length > maxUniqueCharacters) {
      maxUniqueCharacters = currentWord.length;
      wordWithMaxUniqueCharacters = currentWord;
    }
  }
  return wordWithMaxUniqueCharacters;
}

