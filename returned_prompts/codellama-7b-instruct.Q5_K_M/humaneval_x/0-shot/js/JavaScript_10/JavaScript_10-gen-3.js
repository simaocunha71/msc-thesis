/* Test if gniven strig is a palindrome */
const isPalindrome = (string) => {
  return string == string.split('').reverse().join('');
}

/* Find the shortest palindrome that begins with a supplied string.
  Algorithm idea is simple:
  - Find the longest postfix of supplied string that is a palindrome.
  - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
  >>> makePalindrome('')
  ''
  >>> makePalindrome('cat')
  'catac'
  >>> makePalindrome('cata')
  'catac'
  */
const makePalindrome = (string) => {
  const suffix = string.split('').reverse().join('');
  const prefix = string.slice(0, string.length - suffix.length);
  return prefix + suffix.split('').reverse().join('');
}

const test = require('ava');

test('isPalindrome', (t) => {
  t.is(isPalindrome(''), true);
  t.is(isPalindrome('c'), true);
  t.is(isPalindrome('cat'), true);
  t.is(isPalindrome('catac'), true);
  t.is(isPalindrome('catca'), false);
  t.is(isPalindrome('catcacatcac'), true);
});

test('makePalindrome', (t) => {
  t.is(makePalindrome(''), '');
  t.is(makePalindrome('cat'), 'catac');
  t.is(makePalindrome('cata'), 'catac');
  t.is(makePalindrome('catac'), 'catac');
  t.is(makePalindrome('catca'), 'catcacatcac');
  t.is(makePalindrome('catcacatcac'), 'catcacatcac');
});
