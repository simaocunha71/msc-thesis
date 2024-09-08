  let result = [];
  let row_index = 0;
  let col_index = 0;
  while (row_index < lst.length) {
    while (col_index < lst[row_index].length && lst[row_index][col_index] != x) {
      col_index += 1;
    }
    if (col_index < lst[row_index].length) {
      result.push((row_index, col_index));
      col_index += 1;
    }
    row_index += 1;
  }
  return result.sort((a,b) => a[0]-b[0]);
}



