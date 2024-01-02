/*Your task is to implement a function that will simplify the expression
  x * n. The function returns true if x * n evaluates to a whole number and false
  otherwise. Both x and n, are string representation of a fraction, and have the following format,
  <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

  You can assume that x, and n are valid fractions, and do not have zero as denominator.

  simplify("1/5", "5/1") = true
  simplify("1/6", "2/1") = false
  simplify("7/10", "10/2") = false
  */
const simplify = (x, n) => {
  if (x === '0' && n === '1') return 1;
  let a = [];
  let b = n.split('/');
  
  for(let i=1;i<b.length;i++){
    let tempNumerator = x/n.slice(1, -1);
    if (tempNumerator === '0') continue;
    
    a.push(`${tempNumerator}${b[i]}/${x}`);
  }
  
  return !a.find((a)=>!a);
}