const fruitDistribution = (s, n) => {
  const [apples, oranges] = s.split("and").map(Number);
  return n - apples - oranges;
};
