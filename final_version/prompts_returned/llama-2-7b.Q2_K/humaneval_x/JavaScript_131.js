/*Given a positive integer n, return the product of the odd digits.
  Return 0 if all digits are even.
  For example:
  digits(1)  == 1
  digits(4)  == 0
  digits(235) == 15
  */
const digits = (n) => {
  let ans = 0;
  for (let i=0 ; i<n.length ; i+=2){
    let j=i+1,k=j-1;
    if(n[i]%2==1 && n[j]%2==1){
      if(!ans) ans = +n[i];
      ans *= n[i]+n[j] ; 
    }else{
      if(!ans) return '0';
      ans -= (n[i]+n[j]) ;
    }    
  }
  
  return ans;
};
