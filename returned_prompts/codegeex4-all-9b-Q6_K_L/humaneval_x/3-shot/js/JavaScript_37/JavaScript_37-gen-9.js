  var even = [];
  for (var i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      even.push(l[i]);
    }
  }
  even.sort((a, b) => (a - b));
  var result = [];
  for (var i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      result.push(even[Math.floor(i / 2)]);
    } else {
      result.push(l[i]);
    }
  }
  return result;
}