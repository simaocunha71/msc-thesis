  let palindrome = string;

  for (let i = string.length - 1; i >= 0; i--) {
    let postfix = string.substring(i);
    let prefix = string.substring(0, i);
    if (isPalindrome(postfix)) {
      palindrome = prefix + postfix.split('').reverse().join('');
      break;
    }
  }

  return palindrome;
}