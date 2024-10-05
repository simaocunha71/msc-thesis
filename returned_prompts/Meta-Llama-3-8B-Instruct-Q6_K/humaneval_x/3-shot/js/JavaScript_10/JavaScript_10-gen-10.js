  let reversed = string.split('').reverse().join('');
  for (let i = 0; i < string.length; i++) {
    let substr = string.substring(0, i) + reversed;
    if (isPalindrome(substr)) {
      return substr;
    }
  }
  return string + reversed;
}