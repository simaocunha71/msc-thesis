  let sum = 0;
  let is_palindrome = true;

  for (let i = 0; i < q.length; i++) {
    sum += q[i];
    if (q[i] != q[q.length - i - 1]) {
      is_palindrome = false;
    }
  }

  return is_palindrome && sum <= w;
}