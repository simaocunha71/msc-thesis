  let words = S.split(' ');
  let result = 0;
  for (let i = 0; i < words.length; i++) {
    if (words[i] === 'I') {
      if (i + 1 < words.length && (
        words[i + 1] === '.' ||
        words[i + 1] === '?' ||
        words[i + 1] === '!'
      )) {
        result++;
      }
    }
  }
  return result;
}



