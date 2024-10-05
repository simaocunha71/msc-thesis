const prodSigns = (arr) => {
  // If the array is empty, return null
  if (!arr.length) return null;
  // Initialize the product of signs to 1
  let product = 1;
  // Iterate through the array
  for (let i = 0; i < arr.length; i++) {
    // If the current element is 0, multiply the product of signs by 0
    if (arr[i] === 0) product *= 0;
    // If the current element is negative, multiply the product of signs by -1
    else if (arr[i] < 0) product *= -1;
    // If the current element is positive, multiply the product of signs by 1
    else product *= 1;
  }
  // Return the product of signs
  return product;
};

// or

const prodSigns = (arr) => {
  // If the array is empty, return null
  if (!arr.length) return null;
  // Initialize the product of signs to 1
  let product = 1;
  // Iterate through the array
  for (let i = 0; i < arr.length; i++) {
    // If the current element is 0, multiply the product of signs by 0
    if (arr[i] === 0) product *= 0;
    // If the current element is negative, multiply the product of signs by -1
    else product *= arr[i] < 0 ? -1 : 1;
  }
  // Return the product of signs
  return product;
};
