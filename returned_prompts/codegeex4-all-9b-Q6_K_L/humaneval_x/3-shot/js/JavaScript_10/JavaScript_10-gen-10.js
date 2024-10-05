  let postfix = '';
  let i = 0;

  for (i = string.length - 1; i >= 0; i--) {
    postfix = string[i] + postfix;
    if (isPalindrome(postfix)) {
      break;
    }
  }

  let prefix = string.slice(0, i);
  let prefix_reversed = prefix.split('').reverse().join('');
  return string + prefix_reversed;
}



