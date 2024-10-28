  return nthFib(n)
  function nthFib(n) {
    if (n === 1) return 0
    if (n === 2) return 1
    if (n > 2) return nthFib(n - 2) + nthFib(n - 1)
  }
}