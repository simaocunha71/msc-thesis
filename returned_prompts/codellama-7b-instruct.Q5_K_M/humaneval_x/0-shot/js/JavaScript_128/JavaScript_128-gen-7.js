const prodSigns = (arr) => {
  // if empty array return null
  if (!arr.length) return null;
  // if there's only one element, return it
  if (arr.length === 1) return arr[0];
  // if there are more than one element, calculate the product of signs of all elements
  let product = 1;
  for (let i = 0; i < arr.length; i++) {
    // if the current element is positive, set the product to 1
    if (arr[i] > 0) product = 1;
    // if the current element is negative, set the product to -1
    if (arr[i] < 0) product = -1;
    // if the current element is 0, set the product to 0
    if (arr[i] === 0) product = 0;
  }
  // return the product
  return product;
};
