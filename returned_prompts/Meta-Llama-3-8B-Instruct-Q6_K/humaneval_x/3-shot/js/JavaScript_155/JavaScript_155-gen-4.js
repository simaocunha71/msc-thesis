  let evenCount = 0;
  let oddCount = 0;

  for (let i = 0; i < Math.abs(num).toString().length; i++) {
    let digit = parseInt(Math.abs(num).toString()[i]);
    if (digit % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }

  return [evenCount, oddCount];
}
// Test cases
console.log(evenOddCount(-12)); // Output: [1, 1]
console.log(evenOddCount(123)); // Output: [1, 2]