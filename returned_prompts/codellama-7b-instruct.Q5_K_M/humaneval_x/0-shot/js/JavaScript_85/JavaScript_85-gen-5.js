const add = (lst) => {
  if (lst.length === 0) return 0;
  let total = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 === 0) total += lst[i];
  }
  return total;
};

