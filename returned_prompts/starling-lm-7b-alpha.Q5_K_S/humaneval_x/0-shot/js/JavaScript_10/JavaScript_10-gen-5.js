  const stringLength = string.length;

  let palindromeSuffix = string.slice(0);

  while (palindromeSuffix.length && isPalindrome(palindromeSuffix)) {
    palindromeSuffix = palindromeSuffix.slice(0, palindromeSuffix.length - 1);
  }

  const palindromePrefix = string.slice(0, stringLength - palindromeSuffix.length);

  return `${string}${palindromePrefix.split('').reverse().join('')}${palindromeSuffix}`;
};


/* Find the longest palindromic substring in a given string. */
const longestPalindrome = (string) => {
  let longestSubstring = '';

  for (let i = 0; i < string.length; i++) {
    const currentPalindrome = getPalindrome(string, i, i);
    longestSubstring = currentPalindrome.length > longestSubstring.length ? currentPalindrome : longestSubstring;

    for (let j = i + 1; j < string.length; j++) {
      const currentPalindrome = getPalindrome(string, i, j);
      longestSubstring = currentPalindrome.length > longestSubstring.length ? currentPalindrome : longestSubstring;
    }
  }

  return longestSubstring;
};


/* Finds all palindromes in a given string. */
const findAllPalindromes = (string) => {
  const allPalindromes = [];

  for (let i = 0; i < string.length; i++) {
    const currentPalindrome = getPalindrome(string, i, i);
    allPalindromes.push(currentPalindrome);

    for (let j = i + 1; j < string.length; j++) {
      const currentPalindrome = getPalindrome(string, i, j);
      allPalindromes.push(currentPalindrome);
    }
  }

  return allPalindromes;
};


/* Finds the center of a palind