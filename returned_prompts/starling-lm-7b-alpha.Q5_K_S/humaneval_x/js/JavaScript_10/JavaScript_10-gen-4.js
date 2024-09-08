  let palindromic_suffix = string.slice(-1);
  while (!isPalindrome(palindromic_suffix)) {
    palindromic_suffix += string[0];
  }
  return string + palindromic_suffix.slice(0, -1);
}



