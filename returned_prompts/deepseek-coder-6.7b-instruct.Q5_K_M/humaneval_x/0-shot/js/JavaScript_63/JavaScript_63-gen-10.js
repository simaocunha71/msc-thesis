  if(n < 2) {
    return 0;
  } else if(n === 2) {
    return 1;
  }

  let fibfibNums = [0, 0, 1];

  for(let i = 3; i <= n; i++) {
    fibfibNums[i] = fibfibNums[i-1] + fibfibNums[i-2] + fibfibNums[i-3];
  }

  return fibfibNums[n];
}

console.log(fibfib(1)); // 0
console.log(fibfib(5)); // 4
console.log(fibfib(8)); // 24

// The function starts by initializing an array with the first three fibfib numbers.
// It then loops through the rest of the sequence, adding the previous three numbers to the array at each step.
// Finally, it returns the n-th number in the sequence. 
// This approach allows the function to efficiently compute large n-th numbers by storing and reusing previously computed values.
// It has a time complexity of O(n) because it performs a single loop through the sequence from 3 to n, and a space complexity of O(n) because it stores the entire sequence up to the nth number.

// The function is written in JavaScript because it's the programming language used in the question.
// The function uses the JavaScript Array object to store the sequence of fibfib numbers, which allows for efficient random access to elements in the sequence.
// The function uses a for loop to iterate through the sequence from 3 to n, and uses array indexing to access and store the next fibfib number in the sequence.
// The function uses if statements to handle the base cases of the sequence (fibfib(0) and fibfib(1)), which are not stored in the sequence.
// The function returns the n-th fibfib number at the end of the function.
// The function is named fibfib because it's the name of the function.
// The function is exported for use in other JavaScript programs.
// The function is not part of a larger program, so it is not commented on.