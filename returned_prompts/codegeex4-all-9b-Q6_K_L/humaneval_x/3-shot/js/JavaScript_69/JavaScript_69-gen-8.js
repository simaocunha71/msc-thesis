  var count = {};
  for (const n of lst) {
    if (count[n] == undefined) {
      count[n] = 1;
    } else {
      count[n] += 1;
    }
  }

  var max = -1;
  for (const n of Object.keys(count)) {
    if (count[n] >= n && n > max) {
      max = n;
    }
  }
  return max;
}