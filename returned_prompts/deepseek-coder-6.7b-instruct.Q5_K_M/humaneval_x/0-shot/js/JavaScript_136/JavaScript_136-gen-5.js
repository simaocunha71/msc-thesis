  let a = null;
  let b = null;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (a === null || lst[i] > a)) {
      a = lst[i];
    } else if (lst[i] > 0 && (b === null || lst[i] < b)) {
      b = lst[i];
    }
  }
  return [a, b];
}
console.log(largestSmallestIntegers([2, 4, 1, 3, 5, 7])) //== [null, 1]
console.log(largestSmallestIntegers([])) //== [null, null]
console.log(largestSmallestIntegers([0])) //== [null, null]

*/

const largestSmallestIntegers = (lst) => {
  let a = null;
  let b = null;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (a === null || lst[i] > a)) {
      a = lst[i];
    } else if (lst[i] > 0 && (b === null || lst[i] < b)) {
      b = lst[i];
    }
  }
  return [a, b];
}
console.log(largestSmallestIntegers([2, 4, 1, 3, 5, 7])) //== [null, 1]
console.log(largestSmallestIntegers([])) //== [null, null]
console.log(largestSmallestIntegers([0])) //== [null, null]

/*

The function takes in an array of integers as input. It then iterates over each element in the array. If the element is less than zero, it checks if 'a' is null or if the element is greater than 'a'. If these conditions are met, it assigns 'a' the value of the element. If the element is greater than zero, it checks if 'b' is null or if the element is less