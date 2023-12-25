/* Input is a space-delimited string of numberals from 'zero' to 'nine'.
  Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
  Return the string with numbers sorted from smallest to largest
  >>> sortNumbers('three one five')
  'one three five'
  */
const sortNumbers = (numbers) => {
  const newArr = [];
  for(let i = 0, l = numbers.length; i < l; i += 1){
    let nb = numbers[i];
    if (nb === 'zero'){
      continue;
    } else if (!/^[0-9]*$/.test(nb)){ // we have to make sure it is a number so that we don't get an error later on
      console.error(`Input number [${i}] is not valid`);
      return '[]';
    }
    newArr.push(nb);
  }
  const sortedNumbers = newArr.sort(); // use sort() to sort the array numerically
  return `${sortedNumbers.join(' ')}`;
};
