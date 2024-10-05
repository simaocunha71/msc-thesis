const findMax = (words) => {
  let maxUniqueChar = 0;
  let maxUniqueCharWord = "";
  for (let i = 0; i < words.length; i++) {
    let word = words[i];
    if (word.length > maxUniqueChar) {
      maxUniqueChar = word.length;
      maxUniqueCharWord = word;
    }
  }
  return maxUniqueCharWord;
}

