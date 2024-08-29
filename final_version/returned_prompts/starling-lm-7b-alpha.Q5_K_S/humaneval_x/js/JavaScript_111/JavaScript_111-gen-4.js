  let dict = {};

  for (const c of test.split(' ')) {
    if (dict[c]) {
      dict[c] += 1;
    } else {
      dict[c] = 1;
    }
  }

  let max_count = 0;
  let result = {};

  for (const [k, v] of Object.entries(dict)) {
    if (v > max_count) {
      max_count = v;
      result = {};
      result[k] = v;
    } else if (v == max_count) {
      result[k] = v;
    }
  }

  return result;
}



