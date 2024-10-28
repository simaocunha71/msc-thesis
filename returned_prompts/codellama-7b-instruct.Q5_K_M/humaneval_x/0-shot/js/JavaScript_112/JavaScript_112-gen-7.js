const reverseDelete = (s, c) => {
  let deleteChar = '';
  let palindrome = true;
  const result = s.split('').filter(char => {
    if (c.indexOf(char) === -1) {
      deleteChar += char;
      return true;
    }
    palindrome = false;
  });
  return [deleteChar.split('').reverse().join(''), palindrome];
};
