  if (lst.length == 0) return lst;
  lst.sort((a, b) => a - b);
  let res = [];
  let i = 0;
  while (i < lst.length) {
    res.push(lst[i]);
    i++;
    if (i < lst.length) {
      lst.sort((a, b) => b - a);
      res.push(lst[0]);
      lst.shift();
    }
  }
  return res;
}