  let reversed = string.split('').reverse().join('');
  for (let i = string.length; i >= 0; i--) {
    if (isPalindrome(string.substr(0, i))) {
      return string + reversed.substr(i);
    }
  }
}



