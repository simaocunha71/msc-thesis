  I'll use a map to save the results of the previous calls to avoid unnecessary 
  computations. The first call is the one for tri(1) = 3.
  I'll use a function to calculate the result for tri(n)
  */
const tri = (n, memo = {1: 3}) => {
  if (n in memo) return memo[n]
  const result = n % 2 === 0 ? (n + 1) / 2 : tri(n - 1) + tri(n - 2) + tri(n + 1)
  memo[n] = result
  return result
}

