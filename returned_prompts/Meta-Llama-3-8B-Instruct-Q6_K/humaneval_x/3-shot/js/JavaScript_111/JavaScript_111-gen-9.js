  let result = {};
  let max_count = 0;

  if (test === '') {
    return {};
  }

  const words = test.split(' ');
  for (const word of words) {
    const letter = word[0];
    const count = word.length;
    if (count > max_count) {
      result = { [letter]: count };
      max_count = count;
    } else if (count === max_count) {
      result[letter] = count;
    }
  }
  return result;
}