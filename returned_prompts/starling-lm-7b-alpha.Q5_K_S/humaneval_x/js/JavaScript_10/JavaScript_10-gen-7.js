  const isPal = isPalindrome(string);
  if (isPal) {
    return string;
  }
  let prefix = '';
  for (const c of string) {
    prefix += c;
    const suffix = string.slice(string.length - prefix.length);
    const palindrome = prefix + suffix;
    if (isPalindrome(palindrome)) {
      return prefix + suffix + prefix.split('').reverse().join('');
    }
  }
}



