  const palindrome_suffix = string.split('').reverse().join('');
  const palindrome_prefix = palindrome_suffix.split('').slice(0, -1).join('');
  return string + palindrome_prefix + palindrome_suffix;
}



