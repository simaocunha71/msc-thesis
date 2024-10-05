  if (isPalindrome(string)) return string;

  for (let i = 0; i < string.length; i++) {
    if (isPalindrome(string.substring(0, i + 1))) {
      return string.substring(0, i + 1) + string.substring(0, i).split('').reverse().join('');
    }
  }

  return string + string.split('').reverse().join('');
}



