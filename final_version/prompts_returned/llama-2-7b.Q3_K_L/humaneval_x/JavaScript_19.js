/* Input is a space-delimited string of numberals from 'zero' to 'nine'.
  Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
  Return the string with numbers sorted from smallest to largest
  >>> sortNumbers('three one five')
  'one three five'
  */
const sortNumbers = (numbers) => {
  const map = {};
  for (let i = 0; i < numbers.length; ++i) {
    const number = numbers[i];
    map[number] = i; // add a mapping from the given number to its index in the input array
  }

  let result = '';
  let index = -1;
  for (let char of numbers) {
    if (+char >= 0 && +char <= 9) {
      ++index;
      // update char if it's smaller than what we have already seen to get the largest number
      result += map[+char] ? char : 'zero';
      if (++index === numbers.length) break;
    }
  }
  return result;
};
