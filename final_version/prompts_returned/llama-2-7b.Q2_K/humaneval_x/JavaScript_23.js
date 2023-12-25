/* Return length of given string
  >>> strlen('')
  0
  >>> strlen('abc')
  3
  */
const strlen = (string) => {
  return typeof string === 'string' ? string.length : -1;
};