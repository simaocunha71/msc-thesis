  let sum = q.reduce((a, b) => a + b, 0);
  let left = 0;
  let right = q.length - 1;

  while (left < right) {
    if (q[left] != q[right]) {
      return false;
    }
    left += 1;
    right -= 1;
  }

  return sum <= w;
}



