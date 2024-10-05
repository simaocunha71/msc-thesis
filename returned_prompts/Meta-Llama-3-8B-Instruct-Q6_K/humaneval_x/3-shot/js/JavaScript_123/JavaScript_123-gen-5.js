  let result = [n];
  let current = n;
  while (current !== 1) {
    if (current % 2 === 0) {
      current = Math.floor(current / 2);
    } else {
      current = 3 * current + 1;
    }
    if (result.includes(current)) {
      break;
    }
    result.push(current);
  }
  return result.filter(num => num % 2 !== 0).sort((a, b) => a - b);
} // getOddCollatz
// This function returns the list of odd numbers in the Collatz sequence. It starts with the input number and iteratively applies the Collatz sequence rules until it reaches 1. It keeps track of the sequence and breaks when the number is repeated. Finally, it filters out the odd numbers and sorts them in increasing order.