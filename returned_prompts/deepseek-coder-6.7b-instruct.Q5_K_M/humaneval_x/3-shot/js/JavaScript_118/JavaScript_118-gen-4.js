  const vowels = 'AEIOUaeiou';
  for  (let i = word.length - 2; i > 0; i--) {
    if (vowels.includes(word[i + 1]) && vowels.includes(word[i - 1])) {
      return word[i];
    }
  }
  return "";
}



