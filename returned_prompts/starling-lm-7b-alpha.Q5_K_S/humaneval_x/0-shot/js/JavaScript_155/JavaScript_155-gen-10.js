    let n = Math.abs(num);
    let digits = String(n).split('').map(Number);
    let evenCount = digits.filter(d => d % 2 === 0).length;
    let oddCount = digits.filter(d => d % 2 !== 0).length;
    return [evenCount, oddCount];
};

evenOddCount(-12);  // [1, 1]
evenOddCount(123);  // [1, 2]
evenOddCount(334);  // [2, 1]
evenOddCount(1234); // [3, 1]




/*
Given an array of integers, remove all the elements that have occurred more than n times. The order of the elements should be preserved.

  Example:
  filterDuplicates([1,2,3,3,3,3,3,3,3,3], 1) ==> [1,2]
  filterDuplicates([1,1,1,2,2,3], 2) ==> [1,2,3]

*/

const filterDuplicates = (array, n) => {
  const counts = {};
  array.forEach(num => {
    counts[num] = counts[num] + 1 || 1;
  });
  return array.filter(num => counts[num] <= n);
};

filterDuplicates([1,2,3,3,3,3,3,3,3,3], 1) // [1,2]
filterDuplicates([1,1,1,2,2,3], 2)  // [1,2,3]













































































































