const isSimplePower = (x, n) => {
  const int = Math.log(x) / Math.log(n)
  return int % 1 === 0
}
