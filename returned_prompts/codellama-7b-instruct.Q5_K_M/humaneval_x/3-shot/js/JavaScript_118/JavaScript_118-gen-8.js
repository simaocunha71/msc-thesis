  let i = word.length - 1;
  while (i >= 0) {
    if (word[i] === 'a' || word[i] === 'e' || word[i] === 'i' || word[i] === 'o' || word[i] === 'u') {
      if (i > 0 && word[i-1] !== word[i]) {
        return word[i];
      }
      return '';
    }
    i--;
  }
}



