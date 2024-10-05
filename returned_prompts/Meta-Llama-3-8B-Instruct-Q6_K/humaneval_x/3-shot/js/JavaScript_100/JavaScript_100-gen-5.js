  var result = [n];
  for (var i = 1; i < n; i++) {
    var next = result[result.length - 1];
    if (next % 2 === 0) {
      result.push(next + 1);
    } else {
      result.push(next + 2);
    }
  }
  return result;
}