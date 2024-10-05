const oddCount = (lst) => {
  return lst.map(s => s.split('').filter(e => e % 2).length);
}
