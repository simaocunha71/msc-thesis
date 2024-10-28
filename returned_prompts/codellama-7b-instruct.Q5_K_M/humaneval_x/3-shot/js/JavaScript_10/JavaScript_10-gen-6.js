  const prefix = string.split('').reverse().join('');
  const suffix = string.split('').reverse().join('');
  const longest_suffix = findLongestPalindrome(suffix);
  return string + prefix.substr(0, prefix.length - longest_suffix.length) + longest_suffix;
}



