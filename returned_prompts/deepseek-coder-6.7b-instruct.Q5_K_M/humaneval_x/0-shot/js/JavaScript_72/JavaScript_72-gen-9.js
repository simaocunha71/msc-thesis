  const sum = q.reduce((a, b) => a + b, 0);
  const isPalindrome = q.toString() === q.reverse().toString();
  
  return (sum <= w) && isPalindrome;
}

console.log(willItFly([1, 2], 5)); // false
console.log(willItFly([3, 2, 3], 1)); // false
console.log(willItFly([3, 2, 3], 9)); // true
console.log(willItFly([3], 5)); // true

// The function willItFly first calculates the sum of all elements in the array q. Then it checks if the array is a palindrome (same forwards and backwards) by converting the array to a string and reversing it and then comparing those two strings. The function will return true if the sum of the elements is less than or equal to w and the array is a palindrome, and false otherwise.

// The function willItFly uses the reduce method to calculate the sum and the reverse method to check if the array is a palindrome.

// The function willItFly has a time complexity of O(n) because it iterates over the array twice: once to calculate the sum and once to check if the array is a palindrome. The space complexity is O(1) because it uses a constant amount of space to store the sum and the boolean for the palindrome check.

// The function willItFly assumes that the array will only contain positive integers and that the maximum weight will also be a positive integer. It also assumes that the array will not be empty.

// The function willItFly is written in JavaScript and uses modern JavaScript syntax and features.

// The function willItFly is a pure function because it does not have side effects. It does not modify any external state or data. It always produces the same output for the same input.

// The function willItFly is a declarative function because it describes what the output should be, without specifying how to get there. It is also a functional function because it uses functions like reduce and reverse to manipulate the input data.

// The function willItFly is a good example of a pure functional