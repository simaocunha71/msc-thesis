  let counts = {};
  let maxCount = 0;
  let result = {};
  test.split(' ').forEach((letter) => {
    counts[letter] = counts[letter] ? counts[letter] + 1 : 1;
    if (counts[letter] > maxCount) {
      maxCount = counts[letter];
    }
  });
  for (let letter in counts) {
    if (counts[letter] === maxCount) {
      result[letter] = maxCount;
    }
  }
  return result;
}



