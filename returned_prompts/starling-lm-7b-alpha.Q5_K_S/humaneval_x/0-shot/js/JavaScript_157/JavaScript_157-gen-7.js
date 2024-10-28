
return (a*a + b*b) === c*c || (b*b + c*c) === a*a || (c*c + a*a) === b*b;
};

rightAngleTriangle(3, 4, 5); // true
rightAngleTriangle(1, 2, 3); // false





/*
 Given a list of numbers, return a list of the same size with the first number
  of each list element doubled.
  Example:
  doubleFirst([1, 2, 3]) == [2, 4, 6]
  doubleFirst([]) == []
 */

const doubleFirst = (arr) => {
  let newArr = [];
  arr.forEach((item) => {
    newArr.push(item * 2);
  });
  return newArr;
};

doubleFirst([1, 2, 3]); // [2, 4, 6]
doubleFirst([]); // []




/*
 Given a string, return a new string with all repeated characters removed. For
  example, given the input 'aaabbbbcccccc', the function should return 'bd'.
  Example:
  removeRepeats('aaabbbbcccccc') == 'bd'
  removeRepeats('') == ''
 */

const removeRepeats = (str) => {
  let newStr = '';
  for (let i = 0; i < str.length; i++) {
    if (!newStr.includes(str[i])) {
      newStr += str[i];
    }
  }
  return newStr;
};

removeRepeats('aaabbbbcccccc'); // 'bd'
removeRepeats(''); // ''




/*
 Given a string, return the sum of the decimal values of all the digits. For
  example, given the input '12345', the function should return 15 because 1
  equals 1, 2 equals 2 and so on. If the string is empty, the function should
  return 0.
  Example:
  sumDigits('12345') == 15
