  var result = [];
  for (const x of lst) {
    if (x.length % 2 == 0) {
      result.push(x);
    }
  }
  result.sort((a, b) => {
    if (a.length == b.length) {
      return a.localeCompare(b);
    } else {
      return a.length - b.length;
    }
  });
  return result;
}