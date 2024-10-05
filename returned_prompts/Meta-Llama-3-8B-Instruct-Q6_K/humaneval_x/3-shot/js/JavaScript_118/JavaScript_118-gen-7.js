  let result = '';
  for (let i = word.length - 1; i > 0; i--) {
    if (['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'].includes(word[i])) {
      if (['a', 'e', 'i', 'o', 'u'].includes(word[i]) || ['A', 'E', 'I', 'O', 'U'].includes(word[i])) {
        for (let j = i - 1; j >= 0; j--) {
          if (!['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'].includes(word[j])) {
            result = word[i];
            return result;
          }
        }
      }
      return word[i];
    }
  }
  return result;
}