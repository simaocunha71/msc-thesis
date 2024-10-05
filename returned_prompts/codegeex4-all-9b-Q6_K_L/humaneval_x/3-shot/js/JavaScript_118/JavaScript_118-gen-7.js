  const vowels = ['a', 'e', 'i', 'o', 'u'];
  for (let i = word.length - 1; i > 0; i--) {
    if (vowels.includes(word[i]) && !vowels.includes(word[i-1])) {
      return word[i];
    }
  }
  return '';
}

