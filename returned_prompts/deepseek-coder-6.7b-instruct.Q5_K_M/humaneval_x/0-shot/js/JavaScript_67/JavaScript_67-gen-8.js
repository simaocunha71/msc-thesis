  // split the string to get the count of apples and oranges
  let [apples, oranges] = s.split("apples and").map(Number.parseInt);

  // subtract the count of apples and oranges from the total fruits
  // to find the count of mangoes
  let mangoes = n - (apples + oranges);

  return mangoes;
};
*/

const fruitDistribution = (s, n) => {
  let [apples, oranges] = s.split('apples and').map(Number);
  let mangoes = n - (apples + oranges);
  return mangoes;
};

console.log(fruitDistribution('5 apples and 6 oranges', 19)); //8
console.log(fruitDistribution('0 apples and 1 oranges', 3)); //2
console.log(fruitDistribution('2 apples and 3 oranges', 100)); //95
console.log(fruitDistribution('100 apples and 1 oranges', 120)); //19

// output: 8, 2, 95, 19

/*
The function fruitDistribution takes two arguments: a string and an integer. The string
contains the number of apples and oranges in the basket. The integer represents the total
number of fruits in the basket. The function splits the string into the number of apples and
oranges, then subtracts the sum of these numbers from the total number of fruits to find the
number of mangoes. The function returns the number of mangoes.
*/

/*
The function works by first splitting the string into the number of apples and oranges.
The split function splits a string into an array of substrings, and returns the new array.
The function then maps the result to convert each substring to an integer using the
parseInt function. The sum of the apple and orange counts is subtracted from the total
fruit count to find the number of mangoes. The function then returns the number of mangoes.
*/

/*
The function is defined as an arrow function with two parameters: s (the string of fruit
counts) and n (the