/*Circular shift the digits of the integer x, shift the digits right by shift
  and return the result as a string.
  If shift > number of digits, return digits reversed.
  >>> circularShift(12, 1)
  "21"
  >>> circularShift(12, 2)
  "12"
  */
const circularShift = (x, shift) => {
  let digit;
  let str = '';
  if(shift == 'back'){
    digit = -1;
  } else {
    digit = 1;
  }
  while(digit != 0){
    str += String(Math.floor(x % 10));
    x -= Math.floor(x % 10);
    shift--;
    digit++;
  }
  if (shift == -1) {
      str = str[str.length-1] + str.substr(0, str.length-1);
  } else if (shift < 0) {
      console.log('The negative shift is not allowed');
      return 'Error'
}
return str;
};
console.log(circularShift(1234567890,5)); //"907654321"
