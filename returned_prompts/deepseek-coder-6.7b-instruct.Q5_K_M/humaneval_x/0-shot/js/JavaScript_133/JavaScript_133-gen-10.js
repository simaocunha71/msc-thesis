  let result = 0;
  
  for(let i = 0; i < lst.length; i++) {
    let rounded = Math.ceil(lst[i]);
    result += rounded * rounded;
  }
  
  return result;
}

console.log(sumSquares([1,2,3])); // 14
console.log(sumSquares([1,4,9])); // 98
console.log(sumSquares([1,3,5,7])); // 84
console.log(sumSquares([1.4,4.2,0])); // 29
console.log(sumSquares([-2.4,1,1])); // 6


*/

const sumSquares = (lst) => {
  let result = 0;

  for(let i = 0; i < lst.length; i++) {
    let rounded = Math.ceil(lst[i]);
    result += rounded * rounded;
  }

  return result;
}

console.log(sumSquares([1,2,3])); // 14
console.log(sumSquares([1,4,9])); // 98
console.log(sumSquares([1,3,5,7])); // 84
console.log(sumSquares([1.4,4.2,0])); // 29
console.log(sumSquares([-2.4,1,1])); // 6

/*
This JavaScript function will take in a list of numbers as an argument,
iterate through the list, and round each number to the nearest integer using
the Math.ceil() function. It then squares each number and adds it to a running total.
Finally, it returns the total sum of the squared numbers.
*/


/*
