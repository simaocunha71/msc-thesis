/*
  Write a function nextSmallest() that returns the 2nd smallest element of the list.
  Return null if there is no such element.
*/
const nextSmallest = (lst) => {
  const sorted = lst.sort((a, b) => a - b);
  return sorted[1];
}

// TEST CASES
console.log(nextSmallest([1, 2, 3, 4, 5]) === 2); // true
console.log(nextSmallest([5, 1, 4, 3, 2]) === 2); // true
console.log(nextSmallest([]) === null); // true
console.log(nextSmallest([1, 1]) === null); // true
