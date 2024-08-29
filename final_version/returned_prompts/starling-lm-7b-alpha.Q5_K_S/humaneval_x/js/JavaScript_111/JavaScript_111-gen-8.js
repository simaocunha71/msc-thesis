  let dictionary = {};
  for (let i = 0; i < test.length; i++) {
    if (!dictionary[test[i]]) {
      dictionary[test[i]] = 0;
    }
    dictionary[test[i]] += 1;
  }

  let result = {};
  let max_count = 0;
  for (let key in dictionary) {
    if (dictionary[key] > max_count) {
      result = {};
      result[key] = dictionary[key];
      max_count = dictionary[key];
    } else if (dictionary[key] === max_count) {
      result[key] = dictionary[key];
    }
  }

  return result;
}



