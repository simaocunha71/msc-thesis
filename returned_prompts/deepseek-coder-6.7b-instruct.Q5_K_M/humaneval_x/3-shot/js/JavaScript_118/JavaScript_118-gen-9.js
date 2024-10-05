  const vowels = 'aeiouAEIOU';
  let i = word.length - 2;
  while (i > 0) {
    if (vowels.includes(word[i]) && !vowels.includes(word[i - 1]) && !vowels.includes(word[i + 1])) {
      return word[i];
    }
    i--;
  }
  return '';
}



