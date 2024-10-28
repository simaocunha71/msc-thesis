const oddCount = (lst) => {
  return lst.map(str => {
    const arr = str.split('');
    return arr.filter(num => num % 2 === 1).length;
  });
};
