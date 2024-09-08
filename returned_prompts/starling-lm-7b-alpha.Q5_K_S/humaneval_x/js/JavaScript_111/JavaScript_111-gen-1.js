  const letters = {};
  const max = Math.max(...test.split(' ').map((l) => {
    if (!letters[l]) {
      letters[l] = 0;
    }
    letters[l] += 1;
    return letters[l];
  }));

  const result = {};
  for (const letter in letters) {
    if (letters[letter] === max) {
      result[letter] = letters[letter];
    }
  }

  return result;
}



