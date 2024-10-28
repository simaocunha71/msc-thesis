  let str = '';
  for (let i = 0; i < s.length; i++) {
    if (!c.includes(s[i])) {
      str += s[i];
    }
  }
  let isPalindrome = str === str.split('').reverse().join('');
  return [str, isPalindrome];
}



