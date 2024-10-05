
const fruitDistribution = (s, n) => {
  let apples = 0;
  let oranges = 0;
  let mango = n;
  s.split(' ').forEach((fruit) => {
    if (fruit.indexOf('apples') > -1) {
      apples = Number(fruit.split(' ')[0]);
    }
    if (fruit.indexOf('oranges') > -1) {
      oranges = Number(fruit.split(' ')[0]);
    }
  });
  mango -= apples + oranges;
  return mango;
};
