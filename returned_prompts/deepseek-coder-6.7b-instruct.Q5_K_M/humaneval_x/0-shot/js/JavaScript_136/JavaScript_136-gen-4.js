  let neg = null;
  let pos = null;
  
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (neg === null || lst[i] > neg)) {
      neg = lst[i];
    } else if (lst[i] > 0 && (pos === null || lst[i] < pos)) {
      pos = lst[i];
    }
  }
  
  return [neg, pos];
}

console.log(largestSmallestIntegers([2, 4, 1, 3, 5, 7])); // [null, 1]
console.log(largestSmallestIntegers([])); // [null, null]
console.log(largestSmallestIntegers([0])); // [null, null]

This code loops through the list checking if the integer is negative or positive. If it is negative and the current negative maximum is null or less than the current integer, it sets that integer as the new negative maximum. If it is positive and the current positive minimum is null or greater than the current integer, it sets that integer as the new positive minimum. Finally, it returns a list containing the negative maximum and positive minimum.
*/

/*
function largestSmallestIntegers(lst) {
  let neg = null;
  let pos = null;
  
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (neg === null || lst[i] > neg)) {
      neg = lst[i];
    } else if (lst[i] > 0 && (pos === null || lst[i] < pos)) {
      pos = lst[i];
    }
  }
  
  return [neg, pos];
}

console.log(largestSmallestIntegers([2, 4, 1, 3, 5, 7])); // [null, 1]
console.log(largestSmallestIntegers([])); // [null, null]
console.log(largestSmallestIntegers([0])); // [null, null