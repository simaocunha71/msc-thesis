const willItFly = (q, w) => {
  //palindrome check
  if (q.toString() === q.toString().split('').reverse().join('')) {
    //sum check
    let sum = 0;
    for (let i = 0; i < q.length; i++) {
      sum += q[i];
    }
    //max check
    if (sum <= w) {
      return true;
    }
  }
  return false;
}


