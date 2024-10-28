function largestSmallestIntegers(lst) {
  let a = null;
  let b = null;
  let negative = false;
  let positive = false;

  lst.forEach(element => {
    if (element < 0) {
      if (a == null || element > a) {
        a = element;
      }
      negative = true;
    }
    if (element > 0) {
      if (b == null || element < b) {
        b = element;
      }
      positive = true;
    }
  });

  if (positive && negative) {
    return [a, b];
  } else {
    return [null, null];
  }
}

console.log(largestSmallestIntegers([2, 4, 1, 3, 5, 7])); // [null, 1]
console.log(largestSmallestIntegers([])); // [null, null]
console.log(largestSmallestIntegers([0])); // [null, null]


*/
































































































































































































































































