  const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
  const consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';

  for (let i = word.length - 1; i >= 0; i--) {
    if (consonants.includes(word[i])) {
      if (vowels.includes(word[i - 1])) {
        return word[i - 1];
      }
      if (vowels.includes(word[i + 1])) {
        return word[i + 1];
      }
    }
  }

  return "";
}



