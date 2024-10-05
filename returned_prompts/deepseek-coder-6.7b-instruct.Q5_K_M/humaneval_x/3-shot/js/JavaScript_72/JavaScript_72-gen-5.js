  let sum = 0;
  for(let i = 0; i < q.length; i++) {
    sum += q[i];
  }
  let isBalanced = JSON.stringify(q) === JSON.stringify(q.reverse());
  return sum <= w && isBalanced;
}



