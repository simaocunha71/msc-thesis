  let result = [];
  let max = Infinity;
  while (lst.length > 0) {
    let min = lst.reduce((a, b) => a < b ? a : b);
    result.push(min);
    lst = lst.filter(x => x != min);
    max = Math.max(...lst);
    result.push(max);
    lst = lst.filter(x => x != max);
  }
  return result;
}



