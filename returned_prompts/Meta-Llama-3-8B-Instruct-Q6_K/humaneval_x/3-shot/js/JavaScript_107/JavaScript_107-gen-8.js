  let even = 0;
  let odd = 0;
  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    let isEven = true;
    for (let j = 0; j < str.length; j++) {
      if (str[j] !== str[str.length - 1 - j]) {
        isEven = false;
        break;
      }
    }
    if (isEven) {
      even++;
    } else {
      odd++;
    }
  }
  return [even, odd];
}
// test cases:
console.log(evenOddPalindrome(3)); // [1, 2]
console.log(evenOddPalindrome(12)); // [4, 6]