  const words = s.split(' ');
  const result = [];

  for (const word of words) {
    let consonants = 0;
    for (const char of word) {
      if (char.toLowerCase() !== 'a' && char.toLowerCase() !== 'e' && char.toLowerCase() !== 'i' && char.toLowerCase() !== 'o' && char.toLowerCase() !== 'u') {
        consonants++;
      }
    }
    if (consonants === n) {
      result.push(word);
    }
  }

  return result;
}



