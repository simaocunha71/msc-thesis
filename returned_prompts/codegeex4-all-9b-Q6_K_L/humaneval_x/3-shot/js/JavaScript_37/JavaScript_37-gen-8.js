  var even = l.filter((x, i) => i % 2 == 0);
  var sorted = even.sort((a, b) => a - b);
  var result = [];

  var i = 0;
  for (let j = 0; j < l.length; j++) {
    if (j % 2 == 0) {
      result.push(sorted[i]);
      i += 1;
    } else {
      result.push(l[j]);
    }
  }

  return result;
}