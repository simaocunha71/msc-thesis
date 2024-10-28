/*
  Create a function that takes an object, and returns a new object with
  the same values as the original, but with all values incremented by 1.

  increment({ a: 1, b: 2, c: 3 }) ➞ { a: 2, b: 3, c: 4 }
  increment({}) ➞ {}
  */
  const increment = obj => Object.keys(obj).reduce((acc, key) => ({...acc, [key]: obj[key] + 1}), {});

  B:
/*
  Create a function that takes an array of numbers, and returns a new array
  with the first element doubled and the last element halved.

  doubleLast([1, 2, 3]) ➞ [1, 2, 1.5]
  doubleLast([1, 2, 3, 4, 5]) ➞ [1, 2, 3, 4, 2.5]
  doubleLast([1]) ➞ [2]
  */
  const doubleLast = arr => [...arr.slice(0, -1), arr.slice(-1)[0] * 2];

  C:
/*
  Create a function that takes an array of numbers, and returns the sum of all numbers
  in the array, except for the number at index 2, which will be treated as 0.

  sumExceptAtIndex2([1, 2, 3, 4, 5]) ➞ 15
  sumExceptAtIndex2([1, 2, 3, 4, 5, 6]) ➞ 21
  sumExceptAtIndex2([1, 2, 3, 4, 5, 6, 7]) ➞ 28
  */
  const sumExceptAtIndex2 = arr => arr.map((v, i) => (i === 2 ? 0 : v)).reduce((a, b) => a + b, 0);

  D:
/*
  Create a function that takes an array of numbers, and returns a new array
  with the first and last elements removed.

