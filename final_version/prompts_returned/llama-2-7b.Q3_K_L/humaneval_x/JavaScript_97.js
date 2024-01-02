/*Complete the function that takes two integers and returns 
  the product of their unit digits.
  Assume the input is always valid.
  Examples:
  multiply(148, 412) should return 16.
  multiply(19, 28) should return 72.
  multiply(2020, 1851) should return 0.
  multiply(14,-15) should return 20.
  */
const multiply = (a, b) => {
  let x = a % 10;
  let y = b % 10;
  
  const res = x * y;
    
  if(isNaN(res)){
    return null;
  }else{
    return Math.abs(res);
  }
}
