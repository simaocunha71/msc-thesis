  if (lst.length < 2) return null;
  let min = Math.min(...lst);
  let second_min = Math.max(...lst.filter(n => n != min));
  return second_min;
}