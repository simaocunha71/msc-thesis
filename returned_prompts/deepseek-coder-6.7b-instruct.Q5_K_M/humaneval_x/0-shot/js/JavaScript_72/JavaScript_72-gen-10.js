  const isPalindromic = q => q.toString() === q.reverse().toString();
  const sum = q.reduce((a, b) => a + b, 0);
  return isPalindromic(q) && sum <= w;
}

console.log(willItFly([1, 2], 5)); // false
console.log(willItFly([3, 2, 3], 1)); // false
console.log(willItFly([3, 2, 3], 9)); // true
console.log(willItFly([3], 5)); // true

*/

// ----------------------------------

/*
  Write a function that returns true if the array can be sorted into ascending order by only one swap (i.e., with two adjacent elements swapped), and false otherwise.

  Examples:
  oneSwap([3, 2, 1, 5, 4, 7]) ➞ true
  # Elements to swap: 3 and 2

  oneSwap([1, 3, 5, 2, 4, 6]) ➞ true
  # Elements to swap: 5 and 2

  oneSwap([2, 1, 4, 3, 6, 5]) ➞ true
  # Elements to swap: 2 and 4

  oneSwap([5, 4, 3, 2, 1]) ➞ false
  # No two adjacent elements that can be swapped to make the array sorted.

  oneSwap([1, 2, 3, 5, 4]) ➞ false
  # No two adjacent elements that can be swapped to make the array sorted.
*/

const oneSwap = arr => {
  let count = 0;
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      count++;
    }
  }
  return count === 1;
};

console.log(oneSwap([3, 2, 1, 5,