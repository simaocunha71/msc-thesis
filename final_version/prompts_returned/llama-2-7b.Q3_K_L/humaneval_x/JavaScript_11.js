/* Input are two strings a and b consisting only of 1s and 0s.
  Perform binary XOR on these inputs and return result also as a string.
  >>> stringXor('010', '110')
  '100'
  */
const stringXor = (a, b) => {
  let output = '';
  for(let i=0; i < a.length-1; i++){
    if((b[i] === '1')){
      output += '0';
    }else{
      output += '1';
    }
  }
  return output + b[a.length-1];
}
console.log(stringXor('010', '110'));