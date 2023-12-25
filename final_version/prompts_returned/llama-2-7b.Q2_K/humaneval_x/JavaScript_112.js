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
  let deletedString = "";
  for(let i=0;i<c.length;i++){
    if(s.indexOf(c[i]) != -1){//if any character in the passed string is equal to a character in the input string
      let temp = s.split(c); //split the input str on c, so for each iteration of i we get a substring of the original str with an element taken from c
      deletedString += temp[i];// then append each substring to the final result
    }else{deletedString+=' ';}
  }return deletedString;//return the final string
};

module.exports = {reverseDelete};