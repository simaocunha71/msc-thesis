   return string.length;
};
/* Find the index of a given element in a given array
  >>> findIndex([1, 2, 3, 4, 5], 3)
  2
  >>> findIndex([1, 2, 3, 4, 5], 6)
  -1
  */
const findIndex = (arr, element) => {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === element) return i;
  }
  return -1;
};
/* Reverse a given string
  >>> reverse('')
  ''
  >>> reverse('abc')
  'cba'
  */
const reverse = (string) => {
  let new_str = '';
  for (let i = string.length - 1; i >= 0; i--) {
    new_str += string[i];
  }
  return new_str;
};

module.exports = {
  strlen,
  findIndex,
  reverse
};








































































































































































































































































