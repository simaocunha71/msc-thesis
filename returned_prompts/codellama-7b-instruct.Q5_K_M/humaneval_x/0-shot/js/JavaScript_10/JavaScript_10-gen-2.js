const isPalindrome = (string) => {
  return string == string.split('').reverse().join('');
}

const makePalindrome = (string) => {
  let longestPostfixPalindrome = '';
  for (let i = string.length - 1; i >= 0; i--) {
    if (isPalindrome(string.slice(i))) {
      longestPostfixPalindrome = string.slice(i);
      break;
    }
  }
  return string + longestPostfixPalindrome.split('').reverse().join('');
}




