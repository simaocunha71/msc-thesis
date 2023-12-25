/* For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
  Empty sum should be equal to 0 and empty product should be equal to 1.
  >>> sumProduct([])
  (0, 1)
  >>> sumProduct([1, 2, 3, 4])
  (10, 24)
  */
const sumProduct = (numbers, int) => {
  if (!int || !Array.isArray(numbers)) return [0, 1]; // eslint-disable-line no-empty
  const first = numbers[0], secondSum = sumProduct(numbers, first), secondProd = product(first);
  for (let i = 1; i < int.length - 1; i++) {
    if (int[i]) continue; // eslint-disable-line no-continue
    const sum = sumProduct([...secondSum], first) + secondProd, prod = product(first);
    return [sum, prod];
  }
};

/* Calculate the value of the given function and pass the returned value to a callback.
   The function should return an integer.
   >>> calcValue([1, 2, 3], (x) => x + 7) // returns 10
   >>> calcValue([1, 2, -3], (x) => x * -5) // returns -15 */
const calcValue = (list, fn, callback) => list.reduce((v, x, i) => fn(callback)(v, x, i), 0);

/*
  Calculate the area of a rectangle with given dimensions.
*/
const calcArea = calculateRectangleArea;

function calculateRectangleArea(length, width, callback) {
  let sum = length - (width * 2); // The triangle is missing the base
  return [sum];
}

/* Return a function that returns an integer. The function should take three parameters: number to convert,
  number of decimal places desired and how many digits the returned value has.
   >>> parseInt(100)() // returns 1
   >>> parseInt(50)() // returns 50
   >>> parseInt(-2