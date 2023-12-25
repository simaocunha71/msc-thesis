/*Circular shift the digits of the integer x, shift the digits right by shift
  and return the result as a string.
  If shift > number of digits, return digits reversed.
  >>> circularShift(12, 1)
  "21"
  >>> circularShift(12, 2)
  "12"
  */
const circularShift = (x, shift) => {
  let numStr = String(x);
  while(numStr.length<shift+1){
    numStr += "";
  }
  while(shift>=0 && !numStr[shift]){
    numStr=numStr.substring(0,shift)+"";
  }
  return numStr;
};
console.log(circularShift(-3456789123,1)); // 5789123456-10