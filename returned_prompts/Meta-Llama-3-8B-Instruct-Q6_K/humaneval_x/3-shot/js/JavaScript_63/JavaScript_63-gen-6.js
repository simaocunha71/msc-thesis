  if (n <= 1) {
    return 0
  }
  if (n == 2) {
    return 1
  }
  let a = 0, b = 0, c = 1
  for (let i = 3; i <= n; i++) {
    let temp = a + b + c
    a = b
    b = c
    c = temp
  }
  return c
}  // O(n) solution



