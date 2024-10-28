  let result = '';
  for (let i = 0; i < s.length; i++) {
    if (!c.includes(s[i])) {
      result += s[i];
    }
  }
  let isPalindrome = result === result.split('').reverse().join('');
  return [result, isPalindrome];
}



