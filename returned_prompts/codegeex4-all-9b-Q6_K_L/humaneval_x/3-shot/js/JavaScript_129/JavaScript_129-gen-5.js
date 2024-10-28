  var result = [];

  for (const row of grid) {
    for (const cell of row) {
      result.push(cell);
    }
  }

  result.sort((a, b) => a - b);
  result = result.slice(0, k);

  return result;
}