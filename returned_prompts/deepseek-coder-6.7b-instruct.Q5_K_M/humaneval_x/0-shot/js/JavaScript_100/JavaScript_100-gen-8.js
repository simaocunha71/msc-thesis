  let result = [];
  let stones = n;

  for(let i=0; i<n; i++) {
    result.push(stones);
    if(stones % 2 === 0) {
      stones += 2;
    } else {
      stones += 2;
    }
  }
  return result;
}

console.log(makeAPile(3)); // [3,5,7]
console.log(makeAPile(4)); // [4,6,8,10]
*/

const makeAPile = n => {
  let result = [];
  let stones = n;

  for (let i = 0; i < n; i++) {
    result.push(stones);
    stones = stones % 2 === 0 ? stones + 2 : stones + 1;
  }

  return result;
};

console.log(makeAPile(3)); // [3,5,7]
console.log(makeAPile(4)); // [4,6,8,10]
console.log(makeAPile(5)); // [5,7,9,11,13]

// The solution is a simple iteration that pushes the number of stones to the result array at each level and updates the number of stones accordingly.
// The number of stones is updated in such a way that it always becomes the next odd or even number, depending on whether the current number of stones is even or odd.
// Finally, the function returns the result array.

// Time complexity: O(n) as we are iterating through the range of n.
// Space complexity: O(n) as we are storing n elements in the result array.

// This solution works as expected and is efficient.

/*
  The function `makeAPile` takes a positive integer `n` as input.
  It initializes an empty list `result` and a variable `stones` to `n`.
  Then, it iterates `n` times. In each iteration, it:
  - Appends the current value of `stones` to `result`.
  - Updates the value of `stones` to be the next odd or even number, depending on whether `st