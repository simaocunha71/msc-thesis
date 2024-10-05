  var sum = 0;
  for (const e of q) {
    sum += e;
  }

  var isBalanced = true;
  for (let i = 0; i < q.length / 2; i++) {
    if (q[i] != q[q.length - i - 1]) {
      isBalanced = false;
    }
  }

  return sum <= w && isBalanced;
}