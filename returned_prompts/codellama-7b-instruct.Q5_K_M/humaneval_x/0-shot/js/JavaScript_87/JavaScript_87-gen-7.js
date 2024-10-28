  const res = [];

  for (let i = 0; i < lst.length; i++) {
    const row = lst[i];
    const cols = row.length;
    for (let j = 0; j < cols; j++) {
      if (row[j] === x) {
        res.push([i, j]);
      }
    }
  }

  return res;
};
