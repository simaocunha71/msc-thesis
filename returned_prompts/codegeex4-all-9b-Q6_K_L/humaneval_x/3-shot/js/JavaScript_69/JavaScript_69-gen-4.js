  var count = {};

  for (const n of lst) {
    if (n in count) {
      count[n] += 1;
    } else {
      count[n] = 1;
    }
  }

  var result = -1;

  for (const [k, v] of Object.entries(count)) {
    if (v >= k && k > result) {
      result = k;
    }
  }

  return result;
}