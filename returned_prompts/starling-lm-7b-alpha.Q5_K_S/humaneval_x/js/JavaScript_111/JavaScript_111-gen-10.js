  let letters = {};
  for (const letter of test.split(' ')) {
    if (letters[letter] === undefined) {
      letters[letter] = 0;
    }
    letters[letter] += 1;
  }

  let result = {};
  let max_count = 0;
  for (const key in letters) {
    if (letters[key] > max_count) {
      max_count = letters[key];
      result = {};
      result[key] = max_count;
    } else if (letters[key] == max_count) {
      result[key] = letters[key];
    }
  }

  return result;
}



