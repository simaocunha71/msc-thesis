  const vowels = ['a', 'e', 'i', 'o', 'u'];
  const consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';

  for (let i = word.length - 1; i >= 0; i--) {
    if (consonants.includes(word[i])) {
      for (let j = i - 1; j >= 0; j--) {
        if (vowels.includes(word[j])) {
          return word[j];
        }
      }
    }
  }

  return '';
}



