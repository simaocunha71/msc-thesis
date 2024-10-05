  if (n <= 1) {
    return 0
  } else if (n == 2) {
    return 1
  } else {
    let a = 0, b = 0, c = 1
    for (let i = 3; i <= n; i++) {
      let sum = a + b + c
      a = b
      b = c
      c = sum
    }
    return c
  }
}