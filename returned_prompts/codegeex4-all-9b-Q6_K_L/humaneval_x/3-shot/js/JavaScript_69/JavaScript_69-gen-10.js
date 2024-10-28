  var counts = {};

  for (const v of lst) {
    if (counts[v]) {
      counts[v] += 1;
    } else {
      counts[v] = 1;
    }
  }

  var max = -1;
  for (const k in counts) {
    const v = counts[k];
    if (v >= k && v > max) {
      max = v;
    }
  }

  return max;
}