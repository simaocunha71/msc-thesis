/*
  Given a string s, count the number of uppercase vowels in even indices.
  
  For example:
  countUpper('aBCdEf') returns 1
  countUpper('abcdefg') returns 0
  countUpper('dBBE') returns 0
  */
const countUpper = (s) => {
  let index;
  let upperCount = 0;

  while ((index = s.indexOf(s[index - 1].toLowerCase())) > -1) {
    if (upperCount < 2 && index % 2 === 0) {
      upperCount++;
    } else {
      break;
    }
  }
  
  return upperCount;
};
/* 
Given a string s, count the number of lowercase vowels in odd indices.
For example:
countLower('aBCdEf') returns 2
countLower('abcdefg') returns 1
countLower('dBBE') returns 0
*/
const countLower = (s) => {
  let index;
  let lowerCount = 0;
  
  while ((index = s.indexOf(s[index - 1].toUpperCase())) > -1) {
    if (lowerCount < 2 && index % 2 === 1) {
      lowerCount++;
    } else {
      break;
    }
  }
  
  return lowerCount;
};
/*Given a string s, count the number of vowels in indices that aren't even or odd.
For example:
countMixed('aBCdEf') returns 3
countMixed('abcdefg') returns 1
countMixed('dBBE') returns 0
*/
const countMixed = (s) => {
  let count;
  
  for (let i = 2; i < s.length - 1; i++) {
    if (i % 2 !== 0 && i % 2 !== 1) {
      count++;
    } else {
      break;
    }
  }
  
  return count + countUpper(s, {});
};
/*
Given a string s, return true if