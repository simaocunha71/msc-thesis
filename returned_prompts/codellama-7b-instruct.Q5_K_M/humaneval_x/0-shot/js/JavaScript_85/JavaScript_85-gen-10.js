const add = (lst) => {
  return lst.reduce((acc, val, idx) => {
    if (idx % 2 === 0) {
      acc += val;
    }
    return acc;
  }, 0);
};

