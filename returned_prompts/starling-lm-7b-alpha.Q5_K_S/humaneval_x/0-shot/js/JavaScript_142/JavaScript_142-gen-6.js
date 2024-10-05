let result = 0;

for (let i = 0; i < lst.length; i++) {
  if (i % 3 === 0) {
    result += lst[i] ** 2;
  } else if (i % 3 !== 0 && i % 4 === 0) {
    result += lst[i] ** 3;
  }
}

return result;
};

sumSquares([1,2,3]);
sumSquares([]);
sumSquares([-1,-5,2,-1,-5]);


*/

function sumSquares(lst) {
  let result = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 3 === 0) {
      result += lst[i] ** 2;
    } else if (i % 3 !== 0 && i % 4 === 0) {
      result += lst[i] ** 3;
    }
  }
  return result;
}

console.log(sumSquares([1, 2, 3])); 
console.log(sumSquares([]));
console.log(sumSquares([-1, -5, 2, -1, -5]));


*/

function sumSquares(lst) {
  let result = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 3 === 0) {
      result += lst[i] ** 2;
    } else if (i % 3 !== 0 && i % 4 === 0) {
      result += lst[i] ** 3;
    }
  }
  return result;
}

console.log(sumSquares([1, 2, 3])); 
console.log(sumSquares([]));
console.log(sumSquares([-1, -5, 2, -1, -5]));



function sumSquares(lst) {
  let result = 0;
  for (let i