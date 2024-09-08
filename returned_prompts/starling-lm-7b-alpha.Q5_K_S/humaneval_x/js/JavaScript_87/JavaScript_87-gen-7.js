  let result = [];
  for (const row of lst) {
    const index = row.indexOf(x);
    if (index != -1) {
      result.push([row.indexOf(x), row.length - index - 1]);
    }
  }
  result.sort((a, b) => {
    if (a[0] == b[0]) {
      return b[1] - a[1];
    }
    return a[0] - b[0];
  });
  return result;
}



