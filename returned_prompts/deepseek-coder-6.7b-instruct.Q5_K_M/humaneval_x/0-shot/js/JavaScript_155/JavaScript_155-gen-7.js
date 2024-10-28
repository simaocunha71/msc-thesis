  let str = Math.abs(num).toString();
  let evenCount = 0;
  let oddCount = 0;
  for (let i = 0; i < str.length; i++) {
    if (str[i] % 2 == 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }
  return [evenCount, oddCount];
}

console.log(evenOddCount(-12)); //==> [1, 1]
console.log(evenOddCount(123)); //==> [1, 2]
console.log(evenOddCount(1010101)); //==> [6, 0]
console.log(evenOddCount(86420)); //==> [4, 2]
console.log(evenOddCount(13579)); //==> [0, 5]
console.log(evenOddCount(0)); //==> [1, 0]
console.log(evenOddCount(-1234567890)); //==> [5, 5]

*/

function evenOddCount(num) {
  let str = Math.abs(num).toString();
  let evenCount = 0;
  let oddCount = 0;
  for (let i = 0; i < str.length; i++) {
    if (str[i] % 2 == 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  }
  return [evenCount, oddCount];
}

console.log(evenOddCount(-12)); //==> [1, 1]
console.log(evenOddCount(123)); //==> [1, 2]
console.log(evenOddCount(1010101)); //==> [6, 0]
console.log(evenOddCount(86420)); //==> [4, 2]
console.log(evenOddCount(13579)); //==> [0, 5]
console.log(even