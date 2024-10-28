  let t = '';
  for (let ch of s) {
    if (!c.includes(ch)) {
      t += ch;
    }
  }
  let isPalindrome = t === t.split('').reverse().join('');
  return [t, isPalindrome];
}



