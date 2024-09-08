  const palindrome_suffix = (string) => {
    var suffix = string;
    while (suffix.length > 0 && isPalindrome(suffix)) {
      suffix = suffix.slice(0, -1);
    }
    return suffix;
  }

  const reverse_prefix = (string) => {
    var prefix = string.slice(0, -palindrome_suffix(string).length);
    return prefix;
  }

  const palindromic_suffix = palindrome_suffix(string);
  const prefix = reverse_prefix(string);
  const postfix = palindromic_suffix;

  return `${prefix}${postfix}`;
}



