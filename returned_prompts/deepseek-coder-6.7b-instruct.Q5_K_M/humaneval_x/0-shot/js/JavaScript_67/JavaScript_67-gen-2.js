  const [apples, oranges] = s.match(/\d+/g).map(Number);
  return n - apples - oranges;

};

console.log(fruitDistribution("5 apples and 6 oranges", 19));  // 8
console.log(fruitDistribution("0 apples and 1 oranges",3));  // 2
console.log(fruitDistribution("2 apples and 3 oranges", 100));  // 95
console.log(fruitDistribution("100 apples and 1 oranges",120));  // 19

// The regular expression /\d+/g is used to extract the numbers from the string.
// The match() method returns an array of the matches, so we map that array to numbers with the map(Number) function.
// Then we subtract the number of apples and oranges from the total number of fruits to get the number of mangoes.


*/


/*

*/


const fruitDistribution = (s, n) => {
  const [apples, oranges] = s.match(/\d+/g).map(Number);
  return n - apples - oranges;
};

console.log(fruitDistribution("5 apples and 6 oranges", 19));  // 8
console.log(fruitDistribution("0 apples and 1 oranges",3));  // 2
console.log(fruitDistribution("2 apples and 3 oranges", 100));  // 95
console.log(fruitDistribution("100 apples and 1 oranges",120));  // 19

// The regular expression /\d+/g is used to extract the numbers from the string.
// The match() method returns an array of the matches, so we map that array to numbers with the map(Number) function.
// Then we subtract the number of apples and oranges from the total number of fruits to get the number of mangoes.







































