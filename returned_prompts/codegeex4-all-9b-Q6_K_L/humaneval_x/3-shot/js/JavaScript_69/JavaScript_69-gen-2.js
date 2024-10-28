  var frequency = {};
  var max = -1;

  for (const num of lst) {
    if (frequency[num] == undefined) {
      frequency[num] = 1;
    } else {
      frequency[num] += 1;
    }
    if (frequency[num] >= num && num > max) {
      max = num;
    }
  }

  return max;
}



