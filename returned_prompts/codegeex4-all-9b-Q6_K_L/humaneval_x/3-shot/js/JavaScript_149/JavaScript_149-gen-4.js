  var result = [];
  var map = {};

  for (const word of lst) {
    if (word.length % 2 == 0) {
      map[word] = (map[word] || 0) + 1;
    }
  }

  for (const key in map) {
    result.push(key);
  }

  result.sort((a, b) => {
    if (map[a] == map[b]) {
      return a.localeCompare(b);
    } else {
      return map[a] - map[b];
    }
  });

  return result;
}



