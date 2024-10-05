const isSimplePower = (x, n) => {
  return Math.log2(x) % 1 === 0 && Math.log2(x) === Math.log2(n)
}

