/*Given a positive integer n, return the product of the odd digits.
  Return 0 if all digits are even.
  For example:
  digits(1)  == 1
  digits(4)  == 0
  digits(235) == 15
  */
const digits = (n) => {
  let prod = 1;
  for (let i=1 ; i<=n/2; i+=2){
    let x = n%i*i;
    if(x==0){
      break;
    }
    prod *= x;
  }
  return prod > 0 ? prod : 0;
}
