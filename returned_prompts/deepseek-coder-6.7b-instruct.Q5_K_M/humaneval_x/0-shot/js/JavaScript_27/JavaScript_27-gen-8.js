  return string.split('').map(char => {
    return char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
  }).join('');
};

console.log(flipCase('Hello')); // 'hELLO'

Explanation:
This function flips the case of each character in the given string. If the character is uppercase, it converts it to lowercase and vice versa.
*/

const flipCase = (string) => {
  return string.split('').map(char => {
    return char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
  }).join('');
};

console.log(flipCase('Hello')); // 'hELLO'

/*
Tests:

console.log(flipCase('Hello')); // 'hELLO'
console.log(flipCase('hELLO')); // 'Hello'
console.log(flipCase('JavaScript Is Cool')); // 'jAVAsCRIPT iS cOOL'
console.log(flipCase('1234567890')); // '1234567890'
*/


/*
Solution 2:

