
  let result = null;
  if (arr.length === 0) {
    return result;
  }
  result = 0;
  let sign = 1;
  for (let i = 0; i < arr.length; i++) {
    result += sign * Math.abs(arr[i]);
    if (arr[i] < 0) {
      sign *= -1;
    }
  }
  return result;
};

/*
  You are given an array of integers and you need to return
  the product of all the numbers in the array, represented by 1, -1 or 0.
  Note: return null for empty arr.

  Example:
  >>> prodAll( [1, 2, 2, -4] ) == -8
  >>> prodAll([0, 1]) == 0
  >>> prodAll([]) == null
*/

const prodAll = (arr) => {
  let result = null;
  if (arr.length === 0) {
    return result;
  }
  result = 1;
  for (let i = 0; i < arr.length; i++) {
    result *= arr[i];
  }
  return result;
};

/*
  You are given an array of integers. Return a new array with the same length as the input array,
  where each element in the output array is the magnitude of the corresponding element in the input array.

  Note: return null for empty arr.

  Example:
  >>> magArr([1, 2, 2, -4]) == [1, 2, 2, 4]
  >>> magArr([0, 1]) == [0, 1]
  >>> magArr([]) == null

*/

const magArr = (arr) => {
  let result = null;
  if (arr.length === 0) {
    return result;
  }
  result = [];
  for (let i = 0; i < arr.length; i++) {
    result[i] = Math.abs(arr[i]);
  }
  return result;
};

/*
  You are given