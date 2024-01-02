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
  let y;
  if (base === 0){
    x *= Math.pow(8, 3)
    y = `${x}`.slice(-7);
  } else {
    y = String(Math.log10(x)) + ''
    base -= 1
   // y = `${(Math.pow(2, y)).toFixed(0)}`+''
    
  }
  return y;
};