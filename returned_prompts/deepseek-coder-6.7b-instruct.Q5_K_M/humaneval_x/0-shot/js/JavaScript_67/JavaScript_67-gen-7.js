  const [apples, oranges] = s.match(/\d+/g).map(Number);
  return n - apples - oranges;

};
*/

const fruitDistribution = (s, n) => {
  const [apples, oranges] = s.match(/\d+/g).map(Number);
  return n - apples - oranges;
};

console.log(fruitDistribution("5 apples and 6 oranges", 19)); // 8
console.log(fruitDistribution("0 apples and 1 oranges", 3)); // 2
console.log(fruitDistribution("2 apples and 3 oranges", 100)); // 95
console.log(fruitDistribution("100 apples and 1 oranges", 120)); // 19

/*
  The function uses a regular expression to extract the number of apples and oranges from the string.
  Then it subtracts the sum of the apples and oranges from the total number of fruits to find the number of mangoes.
*/

// Test cases
console.log(fruitDistribution("5 apples and 6 oranges", 19)); // 8
console.log(fruitDistribution("0 apples and 1 oranges", 3)); // 2
console.log(fruitDistribution("2 apples and 3 oranges", 100)); // 95
console.log(fruitDistribution("100 apples and 1 oranges", 120)); // 19

// Expected outputs: 8, 2, 95, 19

// This function should return the number of mangoes in the basket based on the total number of fruits and the number of apples and oranges.
// The function uses a regular expression to extract the number of apples and oranges from the string, and then subtracts the sum of the apples and oranges from the total number of fruits to find the number of mangoes.
// The result is then returned by the function.

/*
  The function takes a string and an integer as inputs.
  The string represents the number of apples and oranges in the basket.
  The integer represents the