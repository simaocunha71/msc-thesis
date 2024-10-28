  var count = {};
  lst.forEach(num => {
    if (count[num]) {
      count[num] += 1;
    } else {
      count[num] = 1;
    }
  });

  for (var num in count) {
    if (count[num] >= num) {
      return num;
    }
  }
  return -1;
}