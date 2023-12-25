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
  if (!Array.isArray(arr)) return null;
  let product = arr.reduce((curProduct, currValue) => {
    const prod = Math.abs(currValue) * ((currValue > 0 ? curProduct : -1));
    return [prod + curProduct].join('+');
  }, '(0)');
  
  if (product == '(0)' && arr.length != 0) {
    return -1; // returns null for empty array
  } else {
    const newProduct = product.split('+').reduce((prod, currValue) => {
      prod *= Math.abs(currValue);
      return [Math.abs(currValue) * (prod > 0 ? prod : -1)];
    }, '(0)');
    
    if (!newProduct || newProduct == 'null') product = null;
    else product = newProduct.join('+');
  }
  
  return product || null;
}
