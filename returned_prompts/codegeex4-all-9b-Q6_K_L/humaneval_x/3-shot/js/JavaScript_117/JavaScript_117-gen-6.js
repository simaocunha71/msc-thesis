  let result = [];
  let consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
  let words = s.split(' ');
  for (const word of words) {
    let count = 0;
    for (const c of word) {
      if (consonants.includes(c)) {
        count += 1;
      }
    }
    if (count == n) {
      result.push(word);
    }
  }
  return result;
}

