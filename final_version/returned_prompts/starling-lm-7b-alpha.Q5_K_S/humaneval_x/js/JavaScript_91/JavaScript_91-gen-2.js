  let result = 0;
  let words = S.split(' ');
  for (let i = 0; i < words.length; i++) {
    if (words[i] === 'I') {
      if (i + 1 < words.length && (words[i + 1] === '.' || words[i + 1] === '?' || words[i + 1] === '!' )) {
        result += 1;
      }
    }
  }
  return result;
}



