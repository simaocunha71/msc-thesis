  let words = s.split(' ');
  let result = [];

  for (let word of words) {
    let consonants = 0;
    for (let char of word.toLowerCase()) {
      if (char !== 'a' && char !== 'e' && char !== 'i' && char !== 'o' && char !== 'u' && char !== ' ') {
        consonants++;
      }
    }
    if (consonants === n) {
      result.push(word);
    }
  }

  return result;
}