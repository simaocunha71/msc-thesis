const histogram = (str) => {
  const hist = str.split(' ').reduce((acc, curr) => {
    acc[curr] = (acc[curr] || 0) + 1;
    return acc;
  }, {});
  return hist;
};
