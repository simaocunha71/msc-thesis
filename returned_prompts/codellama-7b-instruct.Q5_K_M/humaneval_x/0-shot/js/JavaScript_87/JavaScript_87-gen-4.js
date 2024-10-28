const getRow = (lst, x) => {

  return lst.reduce((acc, row, rowIdx) => {
    const columns = row.reduce((acc, col, colIdx) => {
      if (col === x) {
        acc.push({ row: rowIdx, col: colIdx });
      }
      return acc;
    }, []).sort((a, b) => b.col - a.col);

    return acc.concat(columns);
  }, []).sort((a, b) => a.row - b.row);
};

console.log(getRow([
  [1, 2, 3, 4, 5, 6],
  [1, 2, 3, 4, 1, 6],
  [1, 2, 3, 4, 5, 1]
], 1));

console.log(getRow([], 1));

console.log(getRow([[], [1], [1, 2, 3]], 3));
