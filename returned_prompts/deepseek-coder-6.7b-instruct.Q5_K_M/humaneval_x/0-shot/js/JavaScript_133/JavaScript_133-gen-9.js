  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    let rounded = Math.ceil(lst[i]);
    sum += Math.pow(rounded, 2);
  }
  return sum;
};

console.log(sumSquares([1,2,3])); // 14
console.log(sumSquares([1,4,9])); // 98
console.log(sumSquares([1,3,5,7])); // 84
console.log(sumSquares([1.4,4.2,0])); // 29
console.log(sumSquares([-2.4,1,1])); // 6

// Explanation:
// For lst = [1,2,3], the rounded numbers are [2,2,3], and the squares are [4,4,9]. The sum is 14.
// For lst = [1,4,9], the rounded numbers are [1,4,9], and the squares are [1,16,81]. The sum is 98.
// For lst = [1,3,5,7], the rounded numbers are [1,3,5,7], and the squares are [1,9,25,49]. The sum is 84.
// For lst = [1.4,4.2,0], the rounded numbers are [2,4,0], and the squares are [4,16,0]. The sum is 29.
// For lst = [-2.4,1,1], the rounded numbers are [0,2,2], and the squares are [0,4,4]. The sum is 6.

// Possible incorrect answers (for reference):
// 1. The code is incorrect because it does not round the numbers to the upper int(Ceiling) first.
// 2. The code is incorrect because it does not square the rounded numbers.
// 3. The code is incorrect because it adds the squares before summing them.
// 4. The code is incorrect because it does not calculate the sum of the squared rounded numbers.
// 