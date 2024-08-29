  let result = [];
  for (const row of lst) {
    for (let i = row.length - 1; i >= 0; i--) {
      if (row[i] === x) {
        result.push([row.indexOf(x), i]);
      }
    }
  }

  result.sort((a, b) => {
    if (a[0] < b[0]) return -1;
    if (a[0] > b[0]) return 1;
    if (a[1] < b[1]) return -1;
    if (a[1] > b[1]) return 1;
    return 0;
  });

  return result;
}



