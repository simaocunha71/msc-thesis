  var sum = 0;
  var isBalanced = true;

  for (const i of q) {
    sum += i;
  }

  for (let i = 0; i < q.length / 2; i++) {
    if (q[i] != q[q.length - 1 - i]) {
      isBalanced = false;
      break;
    }
  }

  return isBalanced && sum <= w;
}