/*
  Write a function that returns true if the object q will fly, and false otherwise.
  The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

  Example:
  willItFly([1, 2], 5) ➞ false
  # 1+2 is less than the maximum possible weight, but it's unbalanced.

  willItFly([3, 2, 3], 1) ➞ false
  # it's balanced, but 3+2+3 is more than the maximum possible weight.

  willItFly([3, 2, 3], 9) ➞ true
  # 3+2+3 is less than the maximum possible weight, and it's balanced.

  willItFly([3], 5) ➞ true
  # 3 is less than the maximum possible weight, and it's balanced.
  */
const willItFly = (q, w) => {
  const [a, b] = q;
  if(Math.max(...b) > Math.min(...a)){return false;}
  for(let i=0, n=w+1;i<n;++i){
    let sum=0, s=Math.abs(a[n-1-i]+b[n-1-i]);
    if(!s)break;
    if((a[n-1-i]%2!==b[n-1-i]%2&&n>=3||n==4&&a[0]%2!==b[0]){return false;}else sum+=s, n--, a=a.splice(0, 2), b=b.splice(0, 2);
    if(!sum)break;
    else switch(n){case 4:sum>=w?true:false;
                      default:if(a[n-1-i]%2!==b[n-1-i]%2&&sum<w){return false;}else sum<=(w/2)?true:false}
  }