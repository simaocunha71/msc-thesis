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
    let stringToReverse = '';
    for(let i= s.length-1; i>=0; i--){
      if(s[i] === c[0]){
        stringToReverse += 'b';
        s = s.substring(0, i) + 'c' + s.substring(i+1);
      }else{
        stringToReverse += s[i];
      }
    }
    return [stringToReverse, reverseDelete(s, c)]
};

const reverseDelete2 = (s, c) => {
  let stringToReverse = '';
  for(let i= s.length-1; i>=0; i--){
    if(c[i] === s[i]){
      stringToReverse += 'a';
      c = c.substring(0, i) + 'e' + c.substring(i+1);
    }else{
      stringToReverse += s[i];
    }
  }
  return [stringToReverse, reverseDelete2(s, c)]
};
console.log(reverseDelete('abcde', 'ae'));
console.log(reverseDelete2('abcdef', 'b'));
