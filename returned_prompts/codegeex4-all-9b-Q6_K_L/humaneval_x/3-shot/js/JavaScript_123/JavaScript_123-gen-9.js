  var result = [];
  var current = n;
  while (current != 1) {
    if (current % 2 == 0) {
      current = current / 2;
    } else {
      current = current * 3 + 1;
    }
    if (current % 2 != 0) {
      result.push(current);
    }
  }
  result.push(1);
  return result.sort();
}



