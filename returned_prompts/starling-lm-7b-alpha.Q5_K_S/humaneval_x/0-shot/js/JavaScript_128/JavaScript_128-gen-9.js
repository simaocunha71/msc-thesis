  if (arr.length === 0) {
    return null;
  }
  let sign = 1;
  let sum = 0;
  let product = 1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 0) {
      product *= 0;
    } else if (arr[i] > 0) {
      sign *= 1;
    } else {
      sign *= -1;
    }
    sum += Math.abs(arr[i]);
  }
  return sign * sum;
};

prodSigns([0, 1]) // 0
prodSigns([1, 2, 2, -4]) // -9
prodSigns([]) // null
*/

// O(n) solution

const prodSigns = (arr) => {
  if (arr.length === 0) {
    return null;
  }
  let sign = 1;
  let sum = 0;
  let product = 1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 0) {
      product *= 0;
    } else if (arr[i] > 0) {
      sign *= 1;
    } else {
      sign *= -1;
    }
    sum += arr[i];
  }
  return sign * sum;
};

prodSigns([0, 1]) // 0
prodSigns([1, 2, 2, -4]) // -9
prodSigns([]) // null

// O(n) solution

*/

