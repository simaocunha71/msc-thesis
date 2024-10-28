const add = (lst) => {
  let sum = 0;
  for (let i = 1; i < lst.length; i += 2) {
    sum += lst[i];
  }
  return sum;
};

