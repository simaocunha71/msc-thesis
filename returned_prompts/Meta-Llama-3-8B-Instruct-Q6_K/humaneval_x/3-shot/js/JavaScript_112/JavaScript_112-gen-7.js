  let result = s.split('');
  for (let i = 0; i < c.length; i++) {
    for (let j = 0; j < result.length; j++) {
      if (result[j] == c[i]) {
        result.splice(j, 1);
        j--;
      }
    }
  }
  let str = result.join('');
  let palindrome = str === str.split('').reverse().join('');
  return [str, palindrome];
}