  let result = [];

  for (const word of s.split(" ")) {
    let consonants = 0;
    for (const c of word) {
      if (isConsonant(c)) {
        consonants += 1;
      }
    }
    if (consonants == n) {
      result.push(word);
    }
  }

  return result;
}



