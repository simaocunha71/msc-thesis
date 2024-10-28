  let even = 0, odd = 0;
  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    if (str === str.split('').reverse().join('')) {
      if (i % 2 === 0) even++;
      else odd++;
    }
  }
  return [even, odd];
}
// or
const evenOddPalindrome = (n) => {
  let even = 0, odd = 0;
  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    if (isPalindrome(str)) {
      if (i % 2 === 0) even++;
      else odd++;
    }
  }
  return [even, odd];
}

function isPalindrome(str) {
  let left = 0, right = str.length - 1;
  while (left < right) {
    if (str[left] !== str[right]) return false;
    left++;
    right--;
  }
  return true;
}
// or
const evenOddPalindrome = (n) => {
  let even = 0, odd = 0;
  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    if (isPalindrome(str)) {
      if (i % 2 === 0) even++;
      else odd++;
    }
  }
  return [even, odd];
}

function isPalindrome(str) {
  let reversed = str.split('').reverse().join('');
  return str === reversed;
}
// or
const evenOddPalindrome = (n) => {
  let even = 0, odd = 0;
  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    if (isPalindrome(str)) {
      if (i % 2 === 0) even++;
      else odd++;
    }
  }
  return [even, odd];
}

function isPalindrome(str) {
  let reversed = str.split('').reverse().join('');
  return str === reversed && str !== reversed.split('').reverse().join('').toString();
}
// or
const evenOddPalindrome = (n) => {
  let even = 0, odd = 0;
  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    if (isPalindrome(str)) {
      if (i % 2 === 