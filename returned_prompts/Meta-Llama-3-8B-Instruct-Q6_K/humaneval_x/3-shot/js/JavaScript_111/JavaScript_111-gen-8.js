  let dict = {};
  if (test === "") {
    return dict;
  }
  test.split(' ').forEach(function(letter) {
    if (dict[letter]) {
      dict[letter]++;
    } else {
      dict[letter] = 1;
    }
  });
  let maxCount = Math.max(...Object.values(dict));
  let result = {};
  Object.keys(dict).forEach(function(key) {
    if (dict[key] === maxCount) {
      result[key] = maxCount;
    }
  });
  return result;
} 



