const sortEven = (l) => {
  const lEven = l.filter((x, i) => i % 2 === 0);
  const lOdd = l.filter((x, i) => i % 2 !== 0);
  return lOdd.concat(lEven.sort());
};