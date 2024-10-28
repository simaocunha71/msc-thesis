  if (isPalindrome(string)) {
    return string;
  }
  const postfix = string.split('').reverse().join('');
  const i = postfix.search(isPalindrome);
  return string + postfix.slice(0, i) + postfix.slice(i).split('').reverse().join('');
}



