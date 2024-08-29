  const countCharacters = (word) => {
    const seen = {};
    for (const c of word) {
      seen[c] = true;
    }
    return Object.keys(seen).length;
  };

  let max_count = 0;
  let max_word = '';
  for (const word of words) {
    const count = countCharacters(word);
    if (count > max_count) {
      max_count = count;
      max_word = word;
    } else if (count === max_count && word < max_word) {
      max_word = word;
    }
  }
  return max_word;
}



