  let max = '';
  let maxCount = 0;
  for (let word of words) {
    let count = new Set(word).size;
    if (count > maxCount) {
      max = word;
      maxCount = count;
    } else if (count === maxCount) {
      if (word < max) {
        max = word;
      }
    }
  }
  return max;
}