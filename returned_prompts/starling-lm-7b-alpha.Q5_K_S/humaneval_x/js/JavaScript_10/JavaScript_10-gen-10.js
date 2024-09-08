  let prefix = '';
  let suffix = string;
  while (!isPalindrome(suffix)) {
    suffix = suffix.slice(1);
    prefix = string.slice(0, prefix.length + 1);
  }
  return string.slice(0, prefix.length) + suffix + prefix.split('').reverse().join('');
}



