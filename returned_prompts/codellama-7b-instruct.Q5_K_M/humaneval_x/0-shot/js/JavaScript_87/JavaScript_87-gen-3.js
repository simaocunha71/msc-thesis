  const rows = [];
  for (let i = 0; i < lst.length; i++) {
    const row = lst[i];
    const columns = [];
    for (let j = 0; j < row.length; j++) {
      if (row[j] === x) {
        columns.push(j);
      }
    }
    if (columns.length) {
      rows.push([i, columns]);
    }
  }
  return rows.sort((a, b) => a[0] - b[0]).map(([row, columns]) => columns.sort((a, b) => b - a).map((column) => [row, column]));
}
