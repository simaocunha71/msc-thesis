  var result = [];
  var num = n;

  while (num != 1) {
    if (num % 2 == 0) {
      num = num / 2;
    } else {
      num = 3 * num + 1;
    }

    if (num % 2 != 0) {
      result.push(num);
    }
  }

  result.push(1);
  return result.sort(function(a, b) {
    return a - b;
  });
}