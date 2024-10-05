  let product = 1;
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 0) {
      product *= 0;
    } else if (arr[i] < 0) {
      product *= -1;
    } else {
      product *= 1;
    }
    sum += Math.abs(arr[i]);
  }
  if (product === 0) {
    return null;
  }
  return product * sum;
};


/*

1, -1, 0 are special cases

1 is +
-1 is -
0 is *

so we need to multiply the absolute value of the array by the product of the sign

ex:

1, 2, 2, -4 = -9
1, 2, -2, 4 = 10
-1, 2, 2, -4 = 8
-1, 2, -2, 4 = -10
0, 2 = 0

*/




























































































































































































































































