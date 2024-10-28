/*
  Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the given array except the one at i.

  For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [6, 3, 2].

  Follow-up: what if you can't use division?

  Hint: Do you know what recursion is?
*/
const arrayProduct = (arr) => {
  if (arr.length === 1) return arr[0];
  const product = arr[0] * arrayProduct(arr.slice(1));
  return product;
};

B:
/*
  Given an array of integers, return a new array where each element is the number of times that
  number appears in the original array.

  For example, the array [1, 2, 3, 2, 1] should be converted to [1, 2, 3, 2, 1].

  For example 2, the array [1, 2, 3, 2, 1] should be converted to [3, 2, 1, 2, 1].
*/
const arrayCount = (arr) => {
  const map = new Map();
  const result = [];
  arr.forEach((item) => {
    if (map.has(item)) {
      map.set(item, map.get(item) + 1);
    } else {
      map.set(item, 1);
    }
  });
  map.forEach((value, key) => {
    result.push(value);
  });
  return result;
};

C:
/*
  Given an array of integers, return a new array where each element is the number of times that
  number appears in the original array.

  For example, the array [1, 2, 3, 2, 1] should be converted to [3, 2, 1