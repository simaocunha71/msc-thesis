  let palindromeEnd = '';

  for (let i = string.length; i >= 0; i--) {
    if (isPalindrome(string.slice(0, i))) {
      palindromeEnd = string.slice(i);
      break;
    }
  }

  return string + palindromeEnd.split('').reverse().join('');
}



