  var result = [];
  for (const n of x) {
    let hasEven = false;
    let digits = n.toString();
    for (const d of digits) {
      if (d % 2 == 0) {
        hasEven = true;
      }
    }
    if (!hasEven) {
      result.push(n);
    }
  }
  return result.sort();
}