/* Concatenate list of strings into a single string
  >>> concatenate([])
  ''
  >>> concatenate(['a', 'b', 'c'])
  'abc'
  */
const concatenate = (strings) => {
  return strings.reduce((accumulator, currentValue) => accumulator + currentValue, '');
}

console.log(concatenate([])); // ''
console.log(concatenate(['a', 'b', 'c'])); // 'abc'