  return arr.sort((a, b) => {
    const aBinary = a.toString(2);
    const bBinary = b.toString(2);
    const aOnes = aBinary.split('1').length - 1;
    const bOnes = bBinary.split('1').length - 1;
    return aOnes - bOnes || a - b;
  });
}

console.log(sortArray([1, 5, 2, 3, 4])); // [1, 2, 3, 4, 5]
console.log(sortArray([-2, -3, -4, -5, -6])); // [-6, -5, -4, -3, -2]
console.log(sortArray([1, 0, 2, 3, 4])); // [0, 1, 2, 3, 4]


*/



//