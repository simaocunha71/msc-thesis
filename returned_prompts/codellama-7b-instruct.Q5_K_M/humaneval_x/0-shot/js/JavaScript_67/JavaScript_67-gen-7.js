const fruitDistribution = (s, n) => {
  let apples = 0;
  let oranges = 0;
  let mango = 0;

  let temp = s.split(' ');

  for (let i = 0; i < temp.length; i++) {
    if (temp[i].indexOf('apples') !== -1) {
      apples = temp[i].split('apples')[0]
    }

    if (temp[i].indexOf('oranges') !== -1) {
      oranges = temp[i].split('oranges')[0]
    }
  }
  mango = n - apples - oranges
  return mango
}
