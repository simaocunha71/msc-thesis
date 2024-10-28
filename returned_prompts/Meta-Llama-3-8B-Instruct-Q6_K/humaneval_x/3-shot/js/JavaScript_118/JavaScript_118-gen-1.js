  for (let i = word.length - 1; i > 0; i--) {
    if (/[aeiouAEIOU]/.test(word[i])) {
      for (let j = i - 1; j >= 0; j--) {
        if (!/[aeiouAEIOU]/.test(word[j])) {
          if (!/[aeiouAEIOU]/.test(word[j + 1])) {
            return word[i];
          }
        } else {
          return word[i];
        }
      }
    }
  }
  return '';
}