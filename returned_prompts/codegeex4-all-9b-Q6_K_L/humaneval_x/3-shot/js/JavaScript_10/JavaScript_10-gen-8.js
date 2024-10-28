  if (isPalindrome(string)) {
    return string;
  }
  for (let i = 0; i < string.length; i++) {
    let prefix = string.slice(0, i);
    let suffix = string.slice(i);
    if (isPalindrome(suffix)) {
      return string + prefix.split('').reverse().join('');
    }
  }
  return string + string.split('').reverse().join('');
}



