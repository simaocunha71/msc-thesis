  let sum = 0;
  let isBalanced = true;
  let reversedQ = q.slice().reverse();

  for (let i = 0; i < q.length; i++) {
    if (q[i] !== reversedQ[i]) {
      isBalanced = false;
      break;
    }
    sum += q[i];
  }

  return isBalanced && sum <= w;
}