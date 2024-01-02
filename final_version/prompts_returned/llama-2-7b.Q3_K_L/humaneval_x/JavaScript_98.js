/*
  Given a string s, count the number of uppercase vowels in even indices.
  
  For example:
  countUpper('aBCdEf') returns 1
  countUpper('abcdefg') returns 0
  countUpper('dBBE') returns 0
  */
const countUpper = (s) => {
  let answer = 0;
  for(let i=0, j = s.length-2; i<j+1;i++){ //go from start to end with increment of 2
    if(s[i] === s[j]){
      answer += 1
    }
  }
  
  return answer
}
