  let min = 0;
  let max = 0;
  let result = [null, null];

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && lst[i] > max) {
      max = lst[i];
    }
    if (lst[i] > 0 && lst[i] < min) {
      min = lst[i];
    }
  }

  if (max === 0) {
    result[0] = null;
  } else {
    result[0] = max;
  }

  if (min === 0) {
    result[1] = null;
  } else {
    result[1] = min;
  }

  return result;
};

console.log(largestSmallestIntegers([2, 4, 1, 3, 5, 7]));  // [null, 1]
console.log(largestSmallestIntegers([]));                // [null, null]
console.log(largestSmallestIntegers([0]));               // [null, null]







































































































































































































































