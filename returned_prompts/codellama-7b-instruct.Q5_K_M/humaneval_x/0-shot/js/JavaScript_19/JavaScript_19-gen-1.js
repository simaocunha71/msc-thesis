/* Input is a space-delimited string of numberals from 'zero' to 'nine'.
  Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
  Return the string with numbers sorted from smallest to largest
  >>> sortNumbers('three one five')
  'one three five'
  */
const sortNumbers = (numbers) => {
  const arr = numbers.split(' ');
  const sorted = arr.sort((a, b) => a - b);
  return sorted.join(' ');
};
