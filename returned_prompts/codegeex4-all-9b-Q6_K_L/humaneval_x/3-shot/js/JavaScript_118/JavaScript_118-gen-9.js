  const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];

  for (let i = word.length - 1; i >= 0; i--) {
    let c = word[i];
    if (vowels.includes(c)) {
      if (i > 0 && i < word.length - 1) {
        if (!vowels.includes(word[i - 1]) && !vowels.includes(word[i + 1])) {
          return c;
        }
      }
    }
  }

  return "";
}