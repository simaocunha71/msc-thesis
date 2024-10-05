  let sum = 0;
  for (let i = 0; i < q.length; i++) {
    sum += q[i];
  }
  let isBalanced = q.join('') === q.reverse().join('');
  return sum <= w && isBalanced;
}



