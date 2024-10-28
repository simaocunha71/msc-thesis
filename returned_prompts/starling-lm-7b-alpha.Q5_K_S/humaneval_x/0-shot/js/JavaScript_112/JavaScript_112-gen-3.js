    let s1 = s.split('').filter(char => !c.includes(char));
    let s2 = s1.reverse().join('');
    return [s2, s2 === s1];
};

/*
  For s = "abcde", c = "ae", the result should be ('bcd',false)
  For s = "abcdef", c = "b"  the result should be ('acdef',false)
  For s = "abcdedcba", c = "ab", the result should be ('cdedc',true)
*/

console.log(reverseDelete("abcde", "ae")); // ("bcd", false)
console.log(reverseDelete("abcdef", "b")); // ("acdef", false)
console.log(reverseDelete("abcdedcba", "ab")); // ("cdedc", true)


*/

/*
Task
  We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
  then check if the result string is palindrome.
  A string is called palindrome if it reads the same backward as forward.
  You should return a tuple containing the result string and true/false for the check.
  Example
  For s = "abcde", c = "ae", the result should be ('bcd',false)
  For s = "abcdef", c = "b"  the result should be ('acdef',false)
  For s = "abcdedcba", c = "ab", the result should be ('cdedc',true)
  */



/*
  For s = "abcde", c = "ae", the result should be ('bcd',false)
  For s = "abcdef", c = "b"  the result should be ('acdef',false)
  For s = "abcdedcba", c = "ab", the result should be ('cdedc',true)
*/

























































