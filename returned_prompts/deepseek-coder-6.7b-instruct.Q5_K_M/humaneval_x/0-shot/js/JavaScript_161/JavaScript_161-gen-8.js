  let reversed = s.split('').map(char => {
    if (char === char.toUpperCase()) return char.toLowerCase();
    else if (char === char.toLowerCase()) return char.toUpperCase();
    else return char;
  }).reverse().join('');

  return reversed;
};

console.log(solve("1234")); // 4321
console.log(solve("ab")); // AB
console.log(solve("#a@C")); // #A@c

/*Explanation:
The function works by splitting the string into an array of characters, reversing that array, and then joining it back together. 
It uses a map function to check the case of each character. 
If the character is uppercase, it changes it to lowercase. 
If it's lowercase, it changes it to uppercase. 
If it's neither (i.e., it's not a letter), it leaves it as it is.
*/


A: You can use a combination of the map function and ternary operator to solve this problem.
Here is a possible solution:


const solve = (s) => {
  return s.split('').map(char => {
    return /[a-z]/i.test(char) ? char.toUpperCase() : char.toLowerCase()
  }).reverse().join('');
};

console.log(solve("1234")); // 4321
console.log(solve("ab")); // AB
console.log(solve("#a@C")); // #A@c


In the code above, the function "solve" takes a string s as input. It splits the string into an array of characters, maps over this array and checks if the character is a letter. If it is, it converts the character to uppercase, otherwise it converts it to lowercase. Then, it reverses the array and joins it back into a string.

A: Here is the solution using JavaScript:


function solve(s) {
    var result = '';
    var isPreviousLetter = false;
    for(var i = s.