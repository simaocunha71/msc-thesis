/*
  Given an array arr of integers, find the minimum number of elements that
  need to be changed to make the array palindromic. A palindromic array is an array that
  is read the same backwards and forwards. In one change, you can change one element to any other element.

  For example:
  smallestChange([1,2,3,5,4,7,9,6]) == 4
  smallestChange([1, 2, 3, 4, 3, 2, 2]) == 1
  smallestChange([1, 2, 3, 2, 1]) == 0
  */
const smallestChange = (arr) => {
  const cache = {};
  const palindrome = (i, j) => {
    if (i > j) {
      return true;
    }
    if (i === j) {
      return true;
    }
    if (cache[i] !== undefined && cache[i] !== undefined) {
      return cache[i] === cache[j];
    }
    if (arr[i] === arr[j]) {
      cache[i] = j;
      cache[j] = i;
      return true;
    }
    for (let k = i + 1; k < j; k++) {
      if (palindrome(i, k) && palindrome(k + 1, j)) {
        cache[i] = k;
        cache[j] = k;
        return true;
      }
    }
    return false;
  };
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] !== arr[j]) {
        count++;
      } else if (arr[i] === arr[j] && i !== j) {
        count += 2;
      }
    }
  }
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {