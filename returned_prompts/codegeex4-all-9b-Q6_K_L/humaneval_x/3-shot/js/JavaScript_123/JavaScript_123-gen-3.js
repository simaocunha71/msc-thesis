  var result = [];
  var current = n;
  while (current != 1) {
    if (current % 2 == 1) {
      result.push(current);
    }
    if (current % 2 == 0) {
      current = current / 2;
    } else {
      current = 3 * current + 1;
    }
  }
  result.push(1);
  return result;
}