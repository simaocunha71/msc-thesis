const add = (lst) => {
  const evenIndices = lst.filter((_, i) => i % 2 === 0);
  return evenIndices.reduce((acc, x) => acc + x, 0);
};


