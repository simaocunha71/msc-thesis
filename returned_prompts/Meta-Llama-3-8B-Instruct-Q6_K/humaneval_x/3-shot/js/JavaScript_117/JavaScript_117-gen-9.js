  let words = s.split(' ');
  let result = [];

  for (let i = 0; i < words.length; i++) {
    let word = words[i];
    let consonants = 0;
    for (let j = 0; j < word.length; j++) {
      if (word[j] !== 'a' && word[j] !== 'e' && word[j] !== 'i' && word[j] !== 'o' && word[j] !== 'u' && word[j] !== ' ') {
        consonants++;
      }
    }
    if (consonants === n) {
      result.push(word);
    }
  }
  return result;
}