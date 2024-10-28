  var result = {};
  var counts = {};

  for (const c of test) {
    if (c == ' ') {
      continue;
    }
    if (c in counts) {
      counts[c] += 1;
    } else {
      counts[c] = 1;
    }
  }

  for (const c in counts) {
    if (Object.keys(result).length == 0) {
      result[c] = counts[c];
    } else if (counts[c] > result[Object.keys(result)[0]]) {
      result = {};
      result[c] = counts[c];
    } else if (counts[c] == result[Object.keys(result)[0]]) {
      result[c] = counts[c];
    }
  }

  return result;
}