  var result = [];
  var num_stones = n;
  for (let i = 0; i < n; i++) {
    result.push(num_stones);
    if (num_stones % 2 == 0) {
      num_stones += 1;
    } else {
      num_stones += 2;
    }
  }
  return result;
}