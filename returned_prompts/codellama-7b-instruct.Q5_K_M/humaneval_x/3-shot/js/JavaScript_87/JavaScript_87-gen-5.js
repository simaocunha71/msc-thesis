  var result = [];
  for (const row of lst) {
    for (let i = 0; i < row.length; i++) {
      if (row[i] == x) {
        result.push([lst.indexOf(row), i]);
      }
    }
  }
  return result;
}



