  lst = lst.filter(x => x !== Math.min(...lst));
  if (lst.length < 2) return null;
  return Math.min(...lst);
}?



