return (a % 10) * (b % 10);
};

/* This function takes an array of integers and returns the
  product of the unit digits of each number. It uses the multiply
  function to calculate each unit digit product.
  Example:
  arrayProduct([148, 412, 19, 28, 2020, 1851, 14, -15]) should return 20.
  arrayProduct([5, 10, 15, 20, 25, 30, 35, 40]) should return 0.
  */

const arrayProduct = (nums) => {

B:
return nums.reduce((acc, curr) => acc * multiply(curr), 1);
};

console.log(arrayProduct([148, 412, 19, 28, 2020, 1851, 14, -15])); // 20
console.log(arrayProduct([5, 10, 15, 20, 25, 30, 35, 40])); // 0


/* This function takes an array of integers and returns the
  product of the unit digits of each number, but only if the
  product is not zero. It uses the multiply function and the arrayProduct
  function to calculate the unit digit product and filter out zeros.
  Example:
  nonZeroProduct([148, 412, 19, 28, 2020, 1851, 14, -15]) should return 16.
  nonZeroProduct([5, 10, 15, 20, 25, 30, 35, 40]) should return 0.
  */

const nonZeroProduct = (nums) => {

C:
return arrayProduct(nums).toString().length % 2 === 0 ? arrayProduct(nums) : 0;
};

console.log(nonZeroProduct([148, 412, 