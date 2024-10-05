return string.split('').map(char => 
  char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase()
).join('');

}

console.log(flipCase('Hello')); // 'hELLO'

Explanation:
The solution first splits the string into an array of characters. Then it maps over each character, checking if it is equal to its uppercase version. If it is, it returns the lowercase version, otherwise it returns the uppercase version. Finally, it joins the array back together into a string.

*/

/*

