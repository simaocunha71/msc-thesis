  let result = [];

  for (const row of lst) {
    if (row.length === 0) {
      continue;
    }
    const index = row.findIndex(i => i === x);
    if (index >= 0) {
      result.push([row.findIndex(i => i === x), index]);
    }
  }

  result.sort((a, b) => {
    if (a[0] === b[0]) {
      return b[1] - a[1];
    }
    return a[0] - b[0];
  });

  return result;
}



