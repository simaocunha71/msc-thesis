const fruitDistribution = (s, n) => {
  let apples = 0;
  let oranges = 0;
  let mango = 0;

  let split = s.split(" ");
  let applesNumber = split[0];
  let orangesNumber = split[2];

  apples = parseInt(applesNumber);
  oranges = parseInt(orangesNumber);

  return n - apples - oranges;
}