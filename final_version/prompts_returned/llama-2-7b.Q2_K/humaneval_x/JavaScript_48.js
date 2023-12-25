/*
  Checks if given string is a palindrome
  >>> isPalindrome('')
  true
  >>> isPalindrome('aba')
  true
  >>> isPalindrome('aaaaa')
  true
  >>> isPalindrome('zbcd')
  false
  */
const isPalindrome = (text) => {
  if (!text.length) return false;
  const map = ['', 'a', 'aa', 'bb', 'ccc']; // add empty string at the front of the array to check if its a palindrome from start
  let j = text.length - 1, ch;
  while ((ch = text[j--]) !== undefined) {
    map.splice(0, 2, text.slice(0, j + 1).map((x) => x === ch ? '' : x), '');
    if (text = map[i] === '') return false; // change the value of map to false when it is not a palindrome from start
  }
  return true;
};

export default function () {
  return {
    isPalindrome,
  };
}
