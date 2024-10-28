  let words = s.split(' ');
  let result = [];

  for (const word of words) {
    let consonants = 0;
    for (const c of word.toLowerCase()) {
      if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != ' ') {
        consonants += 1;
      }
    }
    if (consonants == n) {
      result.push(word);
    }
  }

  return result;
}