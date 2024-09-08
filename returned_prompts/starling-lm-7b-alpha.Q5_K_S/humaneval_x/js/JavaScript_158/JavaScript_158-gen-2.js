  let max_word = "";
  let max_count = 0;

  for (const word of words) {
    let count = 0;
    for (const c of word) {
      if (count.includes(c)) {
        count.push(c);
      } else {
        count.push(c);
      }
    }
    if (count.length > max_count) {
      max_count = count.length;
      max_word = word;
    } else if (count.length == max_count) {
      if (word < max_word) {
        max_word = word;
      }
    }
  }

  return max_word;
}



