  const result = [];
  for (const row of lst) {
    const index = row.indexOf(x);
    if (index >= 0) {
      result.push([row.length, index]);
    }
  }
  result.sort((a, b) => a[0] - b[0]);
  for (const [i, j] of result) {
    result[i] = [i, j];
  }
  return result;
}



