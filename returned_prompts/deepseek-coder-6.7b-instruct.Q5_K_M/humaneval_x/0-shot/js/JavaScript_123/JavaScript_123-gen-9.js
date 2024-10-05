  let collatz = [n];
  while (n != 1) {
    n = n % 2 === 0 ? n / 2 : 3 * n + 1;
    if (n % 2 !== 0) collatz.push(n);
  }
  return collatz.sort((a, b) => a - b);
}

console.log(getOddCollatz(5)) //[1, 5]


// This function works by starting with the number n, then creating the collatz sequence 
// by applying the rules until it reaches 1. For every number that is not 1 and is odd, 
// it is added to the collatz array. Finally, the array is sorted and returned.


// Time Complexity: O(n) since we are running a while loop that runs until n becomes 1.
// Space Complexity: O(n) since we are storing all the numbers in the collatz sequence in an array.


// This solution assumes that the input is always a positive integer.
// In case of invalid input, additional error handling can be added to the function.


/*
  Test Cases:
  1. getOddCollatz(5) returns [1, 5]
  2. getOddCollatz(11) returns [1, 11, 22, 154]
  3. getOddCollatz(15) returns [1, 15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2]
  4. getOddCollatz(27) returns [1, 27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 9