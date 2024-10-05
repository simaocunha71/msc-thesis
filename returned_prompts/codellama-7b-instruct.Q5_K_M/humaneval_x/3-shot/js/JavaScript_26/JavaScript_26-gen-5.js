  var result = [];
  var seen = new Set();

  for (const n of numbers) {
    if (!seen.has(n)) {
      result.push(n);
      seen.add(n);
    }
  }

  return result;
}



