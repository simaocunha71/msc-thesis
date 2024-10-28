
function makePalindrome(string) {
  let longestPostfix = '';
  let longestPrefix = '';
  for (let i = string.length - 1; i >= 0; i--) {
    let postfix = string.slice(i);
    if (isPalindrome(postfix)) {
      longestPostfix = postfix;
      break;
    }
  }
  for (let i = 0; i < string.length; i++) {
    let prefix = string.slice(0, i + 1);
    if (isPalindrome(prefix)) {
      longestPrefix = prefix;
      break;
    }
  }
  return string + longestPrefix.split('').reverse().join('') + longestPostfix;
}

