  var sum = 0;
  var isBalanced = true;
  for (const x of q) {
    sum += x;
    if (x != q[q.length - x]) {
      isBalanced = false;
    }
  }
  return isBalanced && sum <= w;
}