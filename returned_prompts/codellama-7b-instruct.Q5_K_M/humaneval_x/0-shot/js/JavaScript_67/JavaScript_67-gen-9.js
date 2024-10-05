const fruitDistribution = (s, n) => {
  const mango = s.split(' ')[0];
  const oranges = s.split(' ')[1];
  const apples = s.split(' ')[2];
  return n - (oranges * 1) - (apples * 1) + (mango * 1);
};
