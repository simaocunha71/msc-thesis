  let words = s.split(" ");
  let result = [];

  for (const word of words) {
    let count = 0;
    for (const letter of word) {
      if (isConsonant(letter)) {
        count += 1;
      }
    }
    if (count == n) {
      result.push(word);
    }
  }

  return result;
}

function isConsonant(c) {
  return !["a", "e", "i", "o", "u", " "].includes(c);
}



