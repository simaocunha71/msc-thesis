  var result = [];
  var current = n;

  while (current != 1) {
    if (current % 2 == 1) {
      result.push(current);
    }
    current = Math.floor(current / 2);
  }

  result.push(1);
  return result;
}