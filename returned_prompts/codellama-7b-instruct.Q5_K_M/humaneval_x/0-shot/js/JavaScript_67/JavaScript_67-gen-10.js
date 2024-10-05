const fruitDistribution = (s, n) => {
  let apples = s.split(" ")[0];
  let oranges = s.split(" ")[1];
  return n - apples - oranges;
};
