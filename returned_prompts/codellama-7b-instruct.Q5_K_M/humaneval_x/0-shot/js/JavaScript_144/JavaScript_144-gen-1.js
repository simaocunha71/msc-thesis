/*
  The function will take two parameters, x and n, as strings.
  We will first create two variables, num and denom, to store the numerator and denominator of each fraction.
  We will use the split() method to split the strings by the "/" character, and then the join() method to reassemble the split array into a string.
  We will then use the parseInt() method to convert the strings to integers.
  We will then check if the result of the multiplication is an integer by using the remainder() method.
  If the result is not an integer, we will return false.
  If the result is an integer, we will return true.
  */
const simplify = (x, n) => {
  let num1 = x.split('/').join('');
  let num2 = n.split('/').join('');
  let denom = x.split('/').join('');
  let result = parseInt(num1) * parseInt(num2);
  if (result % denom !== 0) return false;
  return true;
};

