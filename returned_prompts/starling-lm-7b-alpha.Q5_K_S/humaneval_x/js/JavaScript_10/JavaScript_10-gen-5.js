  let palindromeSuffix = getPalindromeSuffix(string);
  let palindromePrefix = string.slice(0, string.length - palindromeSuffix.length);

  return palindromePrefix + palindromeSuffix + palindromePrefix.split('').reverse().join('');
}

const getPalindromeSuffix = (string) => {
  let suffix = '';
  for (let i = string.length - 1; i >= 0; i--) {
    if (isPalindrome(string.slice(i))) {
      suffix = string.slice(i);
    }
  }
  return suffix;
}



