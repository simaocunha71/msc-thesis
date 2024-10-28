  const getPalindrome = (num) => {
    const numStr = `${num}`;
    const isPalindrome = numStr === `${numStr}`.split('').reverse().join('');
    if (isPalindrome) {
      return true;
    }
    return false;
  };

  const getEvenPalindrome = (num) => {
    const numStr = `${num}`;
    const isPalindrome = numStr === `${numStr}`.split('').reverse().join('');
    const isEven = num % 2 === 0;
    if (isPalindrome && isEven) {
      return true;
    }
    return false;
  };

  const getOddPalindrome = (num) => {
    const numStr = `${num}`;
    const isPalindrome = numStr === `${numStr}`.split('').reverse().join('');
    const isOdd = num % 2 === 1;
    if (isPalindrome && isOdd) {
      return true;
    }
    return false;
  };

  const palindromes = [];
  for (let i = 1; i < n; i++) {
    if (getPalindrome(i)) {
      if (getEvenPalindrome(i)) {
        palindromes.push(i);
      }
    }
  }
  for (let j = 1; j < n; j++) {
    if (getPalindrome(j)) {
      if (getOddPalindrome(j)) {
        palindromes.push(j);
      }
    }
  }
  return palindromes.length;
};


const test = require('ava');
test('evenOddPalindrome: ', (t) => {
  t.is(evenOddPalindrome(3), [1, 2]);
  t.is(evenOddPalindrome(12), [4, 6]);
});