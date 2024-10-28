  if (!arr.length) {
    return [];
  }
  let minEven = Infinity;
  let minIndex = -1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < minEven) {
      minEven = arr[i];
      minIndex = i;
    }
  }
  if (minIndex === -1) {
    return [];
  }
  return [minEven, minIndex];
}
// test cases
console.log(pluck([4, 2, 3])); // [2, 1]
console.log(pluck([1, 2, 3])); // [2, 1]
console.log(pluck([])); // []
console.log(pluck([5, 0, 3, 0, 4, 2])); // [0, 1]
console.log(pluck([1, 2, 3, 4])); // [2, 1]
console.log(pluck([5, 5, 5])); // []
console.log(pluck([2, 2])); // [2, 0]