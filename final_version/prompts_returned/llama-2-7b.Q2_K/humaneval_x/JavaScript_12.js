/* Out of list of strings, return the longest one. Return the first one in case of multiple
  strings of the same length. Return null in case the input list is empty.
  >>> longest([])

  >>> longest(['a', 'b', 'c'])
  'a'
  >>> longest(['a', 'bb', 'ccc'])
  'ccc'
  */
const longest = (strings) => {
  if (!Array.isArray(strings)) return null;
  const maxLength = strings.reduce((max, curr) => Math.max(...curr), 0);

  for (let i = 1; i < strings.length; i++) {
    if (strings[i].length > maxLength) {
      maxLength = strings[i].length;
    }
  }
  return strings[0];
};

/* Add the two numbers and return the sum. Return null in case of any
  problems, e.g., if either or both arguments are NaN or their string representations
  are empty. */
const sum = (num1, num2) => {
  let sum = parseFloat(String(num1)) + parseFloat(String(num2));
  if (!isNaN(sum)) return sum;
  else return null;
};

/* Add the two numbers and return the sum. Return null in case of any
  problems, e.g., if either or both arguments are NaN or their string representations
  are empty. */
const minus = (num1, num2) => {
  let result = parseFloat(String(num1)) - parseFloat(String(num2));
  if (!isNaN(result)) return result;
  else return null;
};

/* Multiply a number with a string and return the product. Return null in case of
any problems, e.g., if the multiplication yields NaN or the string representation contains
empty or "". */
const multiply = (num1, str) => {
  let prod;
  if (!isNaN(str)) prod = parseFloat(String(num1) * String(str));
  else prod = null;
  return prod;
};

/* Add the two strings and return the sum. Return the first string in case of multiple equal-lengthed