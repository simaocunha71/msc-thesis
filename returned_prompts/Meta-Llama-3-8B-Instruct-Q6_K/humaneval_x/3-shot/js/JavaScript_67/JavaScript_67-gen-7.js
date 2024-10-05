  let [apples, oranges] = s.match(/^(\d+) apples and (\d+) oranges$/).slice(1).map(Number);
  return n - apples - oranges;
}
// Alternative solution:
// const fruitDistribution = (s, n) => {
//   let [_, apples, _, oranges] = s.match(/^.*?(\d+) apples and (\d+) oranges$/).slice(1).map(Number);
//   return n - apples - oranges;
// }