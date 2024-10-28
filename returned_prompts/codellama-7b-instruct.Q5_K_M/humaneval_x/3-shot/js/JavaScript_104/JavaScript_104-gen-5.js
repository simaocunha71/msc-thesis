  var result = [];
  var seen = new Set();

  for (const i of x) {
    if (i % 2 == 1) {
      if (!seen.has(i)) {
        result.push(i);
        seen.add(i);
      }
    }
  }

  return result.sort();
}



