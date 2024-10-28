  let words = s.split(' ');
  let result = [];

  for (let word of words) {
    let consonants = 0;
    for (let char of word) {
      if (char.toLowerCase() != 'a' && char.toLowerCase() != 'e' && char.toLowerCase() != 'i' && char.toLowerCase() != 'o' && char.toLowerCase() != 'u') {
        consonants++;
      }
    }
    if (consonants == n) {
      result.push(word);
    }
  }

  return result;
}