  let total = 0;
  if (arr.length === 0) {
    return null;
  }
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 0) {
      total += 0;
    } else if (arr[i] > 0) {
      total += arr[i];
    } else {
      total -= arr[i];
    }
  }
  return total;
};

*/

/*
  You are given an array arr of integers and you need to return
  sum of magnitudes of integers multiplied by product of all signs
  of each number in the array, represented by 1, -1 or 0.
  Note: return null for empty arr.

  Example:
  >>> prodSigns([1, 2, 2, -4]) == -9
  >>> prodSigns([0, 1]) == 0
  >>> prodSigns([]) == null
  */

function prodSigns(arr) {
  let total = 0;
  if (arr.length === 0) {
    return null;
  }
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 0) {
      total += 0;
    } else if (arr[i] > 0) {
      total += arr[i];
    } else {
      total -= arr[i];
    }
  }
  return total;
}

/*
  You are given an array arr of integers and you need to return
  sum of magnitudes of integers multiplied by product of all signs
  of each number in the array, represented by 1, -1 or 0.
  Note: return null for empty arr.

  Example:
  >>> prodSigns([1, 2, 2, -4]) == -9
  >>> prodSigns([0, 1]) == 0
  >>> prodSigns([]) == null
  */

function prodSigns(arr) {
  let total = 0;
  if (arr.length === 0) {