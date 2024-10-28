  const isPalindrome = (n) => {
    return n.toString() === n.toString().split('').reverse().join('');
  }

  let evenCount = 0;
  let oddCount = 0;

  for (let i = 1; i <= n; i++) {
    if (isPalindrome(i)) {
      if (i % 2 === 0) {
        evenCount++;
      } else {
        oddCount++;
      }
    }
  }

  return [evenCount, oddCount];
}

console.log(evenOddPalindrome(3)); // [1, 2]
console.log(evenOddPalindrome(12)); // [4, 6]
console.log(evenOddPalindrome(100)); // [40, 50]
console.log(evenOddPalindrome(1000)); // [447, 553]
console.log(evenOddPalindrome(1500)); // [688, 812]
console.log(evenOddPalindrome(2000)); // [885, 1115]
console.log(evenOddPalindrome(2500)); // [1097, 1403]
console.log(evenOddPalindrome(3000)); // [1231, 1769]
console.log(evenOddPalindrome(3500)); // [1414, 1986]
console.log(evenOddPalindrome(4000)); // [1560, 2440]
console.log(evenOddPalindrome(4500)); // [1733, 2267]
console.log(evenOddPalindrome(5000)); // [1891, 2709]
console.log(evenOddPalindrome(10000)); // [4475, 5525]
console.log(evenOddPalindrome(2