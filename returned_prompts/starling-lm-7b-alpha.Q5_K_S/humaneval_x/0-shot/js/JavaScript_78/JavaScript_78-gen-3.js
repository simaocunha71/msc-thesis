
  const hexPrimes = {
    "2": false,
    "3": false,
    "4": false,
    "5": true,
    "6": false,
    "7": true,
    "8": false,
    "9": false,
    "A": true,
    "B": true,
    "C": false,
    "D": true,
    "E": false,
    "F": false
  };

  const hexPrimesKeys = Object.keys(hexPrimes);
  let primesCount = 0;

  for (let char of num) {
    if (hexPrimes[char]) {
      primesCount++;
    }
  }

  return primesCount;
};

console.log(hexKey("ABED1A33"));

*/



/*

To solve this problem we will follow these steps:

1. Create an object called `hexPrimes` with hexadecimal digits as keys and boolean values
   that will indicate if the digit is prime or not.
2. Create an array called `hexPrimesKeys` that will store all the keys of `hexPrimes` object.
3. Initialize a variable called `primesCount` to keep track of the number of prime digits found.
4. Iterate through each character of the input string and check if it's a prime digit using the `hexPrimes` object.
5. If the digit is prime, increment the `primesCount` variable.
6. After iterating through all the characters, return the `primesCount` variable.

Here is the code that follows the steps above:

*/


/*

const hexKey = (num) => {

  const hexPrimes = {
    "2": false,
    "3": false,
    "4": false,
    "5": true,
    "6": false,
    "7": true,
    "8": false,
    "9": false,
    "A": true,
    "B": true,
    "C": false,
    "D": true,
    "E": false,
    "F": false
  };
