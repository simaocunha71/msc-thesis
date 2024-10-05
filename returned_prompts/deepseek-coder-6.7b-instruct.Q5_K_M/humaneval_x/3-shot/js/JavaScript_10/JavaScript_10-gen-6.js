  for (let i = string.length - 1; i >= 0; i--) {
    if (isPalindrome(string.substring(0, i + 1))) {
      return string + string.substring(0, string.length - i - 1).split('').reverse().join('');
    }
  }
}



