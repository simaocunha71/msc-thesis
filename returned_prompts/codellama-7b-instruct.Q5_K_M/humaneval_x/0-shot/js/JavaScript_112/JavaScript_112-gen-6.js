/*Task
  We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
  then check if the result string is palindrome.
  A string is called palindrome if it reads the same backward as forward.
  You should return a tuple containing the result string and true/false for the check.
  Example
  For s = "abcde", c = "ae", the result should be ('bcd',false)
  For s = "abcdef", c = "b"  the result should be ('acdef',false)
  For s = "abcdedcba", c = "ab", the result should be ('cdedc',true)
  */
const reverseDelete = (s, c) => {
  let newString = s.split('');
  for (let i = 0; i < newString.length; i++) {
    if (c.includes(newString[i])) {
      newString.splice(i, 1);
      i--;
    }
  }
  newString = newString.join('');
  return [newString, newString.split('').reverse().join('') === newString];
}
B:
const reverseDelete = (s, c) => {
  let result = s.split('');
  result = result.filter(char => !c.includes(char));
  result = result.join('');
  return [result, result.split('').reverse().join('') === result];
}
C:
const reverseDelete = (s, c) => {
  const rev = s.split('').reverse().join('');
  return [s.split('').filter(char => !c.includes(char)).join(''), rev === rev.split('').reverse().join('')];
}
D:
const reverseDelete = (s, c) => {
  const newStr = s.split('').filter(char => !c.includes(char)).join('');
  const revNewStr = newStr.split('').reverse().join('');
  return [newStr, revNewStr === revNewStr.split('').reverse().join('')];
}
E:
const reverseDelete =