const add = (lst) => {
  let res = 0;
  for (let i = 0; i < lst.length; i += 2) {
    res += lst[i];
  }
  return res;
};
