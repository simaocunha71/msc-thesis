  var frequency = {};
  for (const i of lst) {
    if (frequency[i] == undefined) {
      frequency[i] = 1;
    } else {
      frequency[i] += 1;
    }
  }

  var max = -1;
  for (const i of Object.keys(frequency)) {
    if (frequency[i] >= i && i > max) {
      max = i;
    }
  }

  return max;
}