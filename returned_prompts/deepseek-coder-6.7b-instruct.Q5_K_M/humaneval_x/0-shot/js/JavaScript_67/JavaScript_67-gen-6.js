  // parse the input string to get the number of apples and oranges
  const [apples, oranges] = s.match(/\d+/g).map(Number);

  // calculate the number of mangoes by subtracting the number of apples and oranges from the total fruit count
  const mangoes = n - apples - oranges;

  // return the number of mangoes
  return mangoes;
};
*/

// Solution
const fruitDistribution = (s, n) => {
  const [apples, oranges] = s.match(/\d+/g).map(Number);
  const mangoes = n - apples - oranges;
  return mangoes;
};

console.log(fruitDistribution("5 apples and 6 oranges", 19)); // 8
console.log(fruitDistribution("0 apples and 1 oranges", 3)); // 2
console.log(fruitDistribution("2 apples and 3 oranges", 100)); // 95
console.log(fruitDistribution("100 apples and 1 oranges", 120)); // 19
console.log(fruitDistribution("7 apples and 13 oranges", 40)); // 13
console.log(fruitDistribution("30 apples and 2 oranges", 50)); // 18
console.log(fruitDistribution("15 apples and 5 oranges", 30)); // 5
console.log(fruitDistribution("20 apples and 2 oranges", 40)); // 18
console.log(fruitDistribution("50 apples and 0 oranges", 50)); // 50
console.log(fruitDistribution("0 apples and 0 oranges", 10)); // 10
console.log(fruitDistribution("0 apples and 1 oranges", 1)); // 0
console.log(fruitDistribution("1 apples and 1 oranges", 2)); // 0
console.log(fruitDistribution("2 apples and 2 oranges", 4)); // 0

// Expected Output