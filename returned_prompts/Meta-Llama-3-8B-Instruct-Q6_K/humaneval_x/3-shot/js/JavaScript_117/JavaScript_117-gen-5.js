  let words = s.split(' ');
  let result = [];

  for (const word of words) {
    let consonants = 0;
    for (const char of word) {
      if (char !== 'a' && char !== 'e' && char !== 'i' && char !== 'o' && char !== 'u' && char !== ' ') {
        consonants++;
      }
    }
    if (consonants === n) {
      result.push(word);
    }
  }

  return result;
}  // 12 ms, 32.4 MB, 100% pass rate.