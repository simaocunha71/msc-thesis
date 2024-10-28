  let result = '';

  for (const ch of s) {
    if (!c.includes(ch)) {
      result += ch;
    }
  }

  return [result, isPalindrome(result)];
}



