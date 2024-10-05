  let largestNegative = null;
  let smallestPositive = null;
  
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (largestNegative === null || lst[i] > largestNegative)) {
      largestNegative = lst[i];
    }
    if (lst[i] > 0 && (smallestPositive === null || lst[i] < smallestPositive)) {
      smallestPositive = lst[i];
    }
  }
  
  return [largestNegative, smallestPositive];
}

console.log(largestSmallestIntegers([2, 4, 1, 3, 5, 7])) //== [null, 1]
console.log(largestSmallestIntegers([])) //== [null, null]
console.log(largestSmallestIntegers([0])) //== [null, null]

*/

const largestSmallestIntegers = (lst) => {
  let largestNegative = null;
  let smallestPositive = null;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (largestNegative === null || lst[i] > largestNegative)) {
      largestNegative = lst[i];
    }
    if (lst[i] > 0 && (smallestPositive === null || lst[i] < smallestPositive)) {
      smallestPositive = lst[i];
    }
  }

  return [largestNegative, smallestPositive];
}

console.log(largestSmallestIntegers([2, 4, 1, 3, 5, 7])) //== [null, 1]
console.log(largestSmallestIntegers([])) //== [null, null]
console.log(largestSmallestIntegers([0])) //== [null, null]

/*
This code iterates through the list, checking each number to see if it is negative and
if it is greater than the current largestNegative, or if it