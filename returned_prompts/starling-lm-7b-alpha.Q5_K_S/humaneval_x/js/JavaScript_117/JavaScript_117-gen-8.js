  let words = s.split(' ');
  let result = [];

  for (const word of words) {
    let count = 0;
    for (const c of word) {
      if (!('aeiou'.includes(c.toLowerCase()))) {
        count += 1;
      }
      if (count == n) {
        result.push(word);
      }
    }
  }

  return result;
}



