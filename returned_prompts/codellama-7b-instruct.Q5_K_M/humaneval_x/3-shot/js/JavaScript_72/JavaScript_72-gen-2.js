  let sum = 0;
  let isPalindromic = true;
  let isBalanced = true;

  if (q.length % 2 == 1) {
    isBalanced = false;
  }

  for (let i = 0; i < q.length; i++) {
    sum += q[i];
    if (sum > w) {
      isBalanced = false;
      break;
    }
    if (q[i] != q[q.length - i - 1]) {
      isPalindromic = false;
      break;
    }
  }

  return isPalindromic && isBalanced && sum <= w;
}



