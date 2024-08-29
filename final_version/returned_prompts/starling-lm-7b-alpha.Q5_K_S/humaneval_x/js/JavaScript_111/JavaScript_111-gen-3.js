  let result = {};
  let letters = test.split(' ');

  for (let i = 0; i < letters.length; i++) {
    if (result[letters[i]] === undefined) {
      result[letters[i]] = 1;
    } else {
      result[letters[i]] += 1;
    }
  }

  return result;
}



