  if (isPalindrome(string)) {
    return string;
  }

  for (let i = 0; i < string.length; i++) {
    let postfix = string.slice(i);
    if (isPalindrome(postfix)) {
      let prefix = string.slice(0, i);
      return string + prefix.split('').reverse().join('');
    }
  }
}



