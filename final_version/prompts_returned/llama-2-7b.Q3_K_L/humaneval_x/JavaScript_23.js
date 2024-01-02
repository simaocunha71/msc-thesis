/* Return length of given string
  >>> strlen('')
  0
  >>> strlen('abc')
  3
  */
const strlen = (string) => {
  let sLen = 0;
  for (let i=0 ; i<string.length ; i++) {sLen++;}
  return(sLen);
};