  let str = s.split('').filter(x => !c.includes(x)).join('');
  let isPalindrome = str === str.split('').reverse().join('');
  return [str, isPalindrome];
}



