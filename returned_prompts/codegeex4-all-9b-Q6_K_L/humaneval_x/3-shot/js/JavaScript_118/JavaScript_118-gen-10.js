  const vowels = ['a', 'e', 'i', 'o', 'u'];
  const consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'];

  for (let i = word.length - 1; i >= 0; i--) {
    if (consonants.includes(word[i])) {
      if (vowels.includes(word[i - 1])) {
        return word[i - 1];
      }
    }
  }

  return "";
}