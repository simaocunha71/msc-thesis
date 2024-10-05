  var result = [];
  var i = 1;
  while (result.length < n) {
    if (i % 2 === 0) {
      result.push(i);
    } else {
      result.push(i - 1);
    }
    i += 1;
  }
  return result;
}