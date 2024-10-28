
  let result = [];
  for(let i = 0; i < game.length; i++){
    result.push(Math.abs(game[i] - guess[i] ) )
  }
  return result;
}

console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) //  [0,0,0,0,3,3]
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) //  [4,4,1,0,0,6]

The function takes in two arrays and compares each element in the arrays at the same index. It subtracts the guess from the score, then takes the absolute value to ensure the result is always positive. It then pushes the result into a new array which is returned at the end.

*/



//Testing
console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) //  [0,0,0,0,3,3]
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) //  [4,4,1,0,0,6]




/*
//Testing
console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) //  [0,0,0,0,3,3]
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) //  [4,4,1,0,0,6]
*/


/*
//Testing
console.log(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) //  [0,0,0,0,3,3]
console.log(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) //  [4