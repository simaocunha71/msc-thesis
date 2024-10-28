  var sum = 0;
  for (const x of q) {
    sum += x;
  }

  if (sum > w) {
    return false;
  }

  for (let i = 0; i < q.length; i++) {
    if (q[i] != q[q.length - 1 - i]) {
      return false;
    }
  }

  return true;
}



