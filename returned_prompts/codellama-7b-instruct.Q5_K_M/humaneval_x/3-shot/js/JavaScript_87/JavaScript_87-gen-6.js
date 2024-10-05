  const rows = [];

  for (let i = 0; i < lst.length; i++) {
    const row = lst[i];
    const columns = [];
    for (let j = 0; j < row.length; j++) {
      if (row[j] === x) {
        columns.push(j);
      }
    }
    if (columns.length > 0) {
      rows.push([i, ...columns]);
    }
  }

  rows.sort((a, b) => a[0] - b[0]);
  rows.sort((a, b) => b[1] - a[1]);

  return rows;
}



