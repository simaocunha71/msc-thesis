  if (arr.length === 0) return null;
  let result = 0;
  let sign = 1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 0) {
      result += 0;
    } else if (arr[i] > 0) {
      result += arr[i] * sign;
    } else {
      result += arr[i] * sign * -1;
    }
    sign *= arr[i];
  }
  return result;
};

prodSigns([1, 2, 2, -4]);
prodSigns([0, 1]);
prodSigns([]);




















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


const prodSigns = (arr) => {

  if (arr.length === 0) return null;
  let result = 0;
  let sign = 1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 0) {
      result += 0;
    } else if (arr[i] > 0) {
      result += arr[i] * sign;
    } else {
      result += arr[i] * sign * -1;
    }
    sign *= arr[i];
  }
  return result;
};



























































