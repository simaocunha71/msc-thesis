  var result = [];
  var current = 2;
  while (n > 1) {
    var count = 0;
    while (n % current == 0) {
      n /= current;
      count++;
    }
    if (count > 0) {
      for (let i = 0; i < count; i++) {
        result.push(current);
      }
    }
    current++;
  }
  return result;
}