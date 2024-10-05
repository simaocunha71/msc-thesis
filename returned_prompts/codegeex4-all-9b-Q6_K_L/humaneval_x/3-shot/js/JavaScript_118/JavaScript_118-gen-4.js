  const vowels = 'aeiou';
  let last = word.length - 1;
  while (last > 0) {
    if (vowels.includes(word[last])) {
      return word[last];
    }
    if (vowels.includes(word[last - 1])) {
      return '';
    }
    last -= 1;
  }
  return '';
}



