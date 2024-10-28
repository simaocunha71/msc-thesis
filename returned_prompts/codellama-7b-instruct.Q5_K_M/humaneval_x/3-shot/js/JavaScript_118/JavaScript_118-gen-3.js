  let vowels = ['a', 'e', 'i', 'o', 'u'];

  for (let i = 0; i < word.length; i++) {
    if (vowels.includes(word[i])) {
      if (word[i - 1] !== undefined && word[i - 1] !== vowels.includes(word[i - 1])) {
        if (word[i + 1] !== undefined && word[i + 1] !== vowels.includes(word[i + 1])) {
          return word[i];
        }
      }
    }
  }

  return '';
}



