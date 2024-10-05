  var result = [];
  for (var i = 0; i < n; i++) {
    if (n % 2 == 0) {
      result.push(n + 1);
    } else {
      result.push(n + 2);
    }
    n += 2;
  }

  return result;
}



