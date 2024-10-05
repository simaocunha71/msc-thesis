  var result = [n];
  var level = 1;
  var count = n;

  while (count > 0) {
    if (level % 2 == 0) {
      result.push(count);
      count += 1;
    } else {
      result.push(count);
      count += 2;
    }
    level += 1;
  }

  return result;
}