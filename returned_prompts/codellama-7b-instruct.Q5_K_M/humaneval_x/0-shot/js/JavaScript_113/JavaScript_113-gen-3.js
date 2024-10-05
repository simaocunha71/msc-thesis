const oddCount = (lst) => {
  return lst.map(str => {
    return str.split('').filter(digit => digit % 2 !== 0).length;
  });
};

B:
const oddCount = (lst) => {
  return lst.map(str => {
    return str.split('').reduce((acc, digit) => {
      return digit % 2 !== 0 ? ++acc : acc;
    }, 0);
  });
};

C:
const oddCount = (lst) => {
  return lst.map(str => {
    return str.split('').filter(digit => digit % 2 === 1).length;
  });
};

D:
const oddCount = (lst) => {
  return lst.map(str => {
    return str.split('').reduce((acc, digit) => {
      return digit % 2 === 1 ? ++acc : acc;
    }, 0);
  });
};
