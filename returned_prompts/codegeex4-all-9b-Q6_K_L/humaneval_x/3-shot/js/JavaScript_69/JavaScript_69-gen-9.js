  var frequency = {};
  for (let i = 0; i < lst.length; i++) {
    if (frequency[lst[i]] != undefined) {
      frequency[lst[i]] += 1;
    } else {
      frequency[lst[i]] = 1;
    }
  }

  var max = -1;
  for (const key in frequency) {
    if (frequency[key] >= key) {
      if (key > max) {
        max = key;
      }
    }
  }

  return max;
}