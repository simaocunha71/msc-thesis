const add = (lst) => {
  return lst.filter((x, i) => i % 2 === 0).reduce((a, x) => a + x, 0);
};

