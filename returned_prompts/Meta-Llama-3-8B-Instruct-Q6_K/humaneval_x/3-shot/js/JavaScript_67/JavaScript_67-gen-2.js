  let [apples, oranges] = s.match(/(\d+) (apples|oranges)/g).map(x => parseInt(x.match(/\d+/)[0]));
  return n - apples - oranges;
}
// Alternative solution
const fruitDistribution = (s, n) => {
  let [_, apples, oranges] = s.match(/(\d+) (apples|oranges)/g).map(x => parseInt(x.match(/\d+/)[0]));
  return n - apples - oranges;
}