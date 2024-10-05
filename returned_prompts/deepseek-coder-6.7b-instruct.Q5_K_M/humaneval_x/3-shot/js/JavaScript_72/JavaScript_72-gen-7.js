  let sum 		= 0;
  let isPalindrome = true;
  for(let i = 0; i < q.length / 2; i++) {
    if(q[i] !== q[q.length - 1 - i]) {
      isPalindrome = false;
      break;
    }
  }
  if(isPalindrome) {
    for(let i = 0; i < q.length; i++) {
      sum += q[i];
    }
    if(sum <= w) {
      return true;
    }
  }
  return false;
}



