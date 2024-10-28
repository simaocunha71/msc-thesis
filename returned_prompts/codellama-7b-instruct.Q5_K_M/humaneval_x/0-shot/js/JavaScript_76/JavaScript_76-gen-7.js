const isSimplePower = (x, n) => {
  return x === n ** Math.floor(Math.log2(n))
}

/*
  The idea is to use Math.log2 to get the power of n in x.
  To get the power we need to use the floor function.
  */

