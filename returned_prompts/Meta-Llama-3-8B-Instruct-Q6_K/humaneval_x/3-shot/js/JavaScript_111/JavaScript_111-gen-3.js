  let result = {};
  let max_count = 0;
  let max_letter = '';

  if (test === '') {
    return {};
  }

  let words = test.split(' ');
  for (let word of words) {
    let letter_count = {};
    for (let letter of word) {
      if (letter_count[letter]) {
        letter_count[letter] += 1;
      } else {
        letter_count[letter] = 1;
      }
    }
    for (let letter in letter_count) {
      if (letter_count[letter] > max_count) {
        max_count = letter_count[letter];
        max_letter = letter;
        result = { [max_letter]: max_count };
      } else if (letter_count[letter] == max_count) {
        if (!result[letter]) {
          result[letter] = max_count;
        }
      }
    }
  }
  return result;
}