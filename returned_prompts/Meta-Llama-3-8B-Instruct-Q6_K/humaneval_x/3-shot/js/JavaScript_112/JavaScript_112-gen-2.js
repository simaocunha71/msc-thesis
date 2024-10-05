  let result = '';
  for (const char of s) {
    if (!c.includes(char)) {
      result += char;
    }
  }
  return [result, result === result.split('').reverse().join('')];
} // The second element of the returned array is a boolean indicating whether the result string is a palindrome.