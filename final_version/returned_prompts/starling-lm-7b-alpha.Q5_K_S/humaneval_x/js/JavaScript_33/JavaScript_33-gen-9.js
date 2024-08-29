  let result = [];
  for (const i of l) {
    if (i % 3 == 0) {
      result.push(l.sort(function(a, b) { return a - b }));
    } else {
      result.push(i);
    }
  }
  return result;
}



