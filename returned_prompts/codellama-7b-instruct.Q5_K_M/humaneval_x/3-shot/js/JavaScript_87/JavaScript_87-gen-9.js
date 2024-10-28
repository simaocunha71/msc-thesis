  var result = [];
  for (let row_index = 0; row_index < lst.length; row_index++) {
    for (let col_index = 0; col_index < lst[row_index].length; col_index++) {
      if (lst[row_index][col_index] === x) {
        result.push([row_index, col_index]);
      }
    }
  }
  result.sort((a, b) => a[0] - b[0]);
  result.sort((a, b) => b[1] - a[1]);
  return result;
}



