  let arr = s.split("");
  let reversed = arr.map(char => {
    if(char === char.toUpperCase() && isNaN(char)){
      return char.toLowerCase();
    } else if(char === char.toLowerCase() && isNaN(char)){
      return char.toUpperCase();
    } else {
      return char;
    }
  });
  return reversed.join("");
};

console.log(solve("1234")) // "4321"
console.log(solve("ab")) // "AB"
console.log(solve("#a@C")) // "#A@c"

*/

// Alternative Solution:

const solve = s => {
  return s === s.toUpperCase() 
    ? s.toLowerCase() 
    : s.split('').map(c => c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase()).join('');
};

console.log(solve("1234")) // "4321"
console.log(solve("ab")) // "AB"
console.log(solve("#a@C")) // "#A@c"






















































































































































































































