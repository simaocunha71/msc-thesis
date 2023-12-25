/*Change numerical base of input number x to base.
  return string representation after the conversion.
  base numbers are less than 10.
  >>> changeBase(8, 3)
  '22'
  >>> changeBase(8, 2)
  '1000'
  >>> changeBase(7, 2)
  '111'
  */
const changeBase = (x, base) => {
  let output = '';
  for (let i = 0; i < x; i++) {
    if ((i + base - 1) % base != 0 && (i + base) % base == 0) {
      output += String(i + base);
    } else {
      output += String((i + base));
    }
  }

  return output;
};
