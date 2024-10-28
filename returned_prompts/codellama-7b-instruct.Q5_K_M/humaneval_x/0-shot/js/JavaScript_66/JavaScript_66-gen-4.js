/*
  The task is to return the sum of the upper characters' ASCII codes.
  The input string can be empty.
  The sum of the ASCII codes can be 0 if the input is empty.
  */
  const upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  let sum = 0
  for (let i = 0; i < s.length; i++) {
      if (upperCase.includes(s[i])) {
          sum += s[i].charCodeAt(0)
      }
  }
  return sum
};
