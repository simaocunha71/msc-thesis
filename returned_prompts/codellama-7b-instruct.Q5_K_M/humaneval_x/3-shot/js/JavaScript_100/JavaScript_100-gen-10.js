  var result = [n];
  for (var i = 1; i < n; i++) {
    n = (n % 2 == 0) ? n + 1 : n + 2;
    result.push(n);
  }
  return result;
}



