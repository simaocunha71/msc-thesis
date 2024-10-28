const prodSigns = (arr) => {
  if (!arr.length) return null
  let sum = 0
  let prod = 1
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) prod *= -1
    sum += Math.abs(arr[i]) * prod
    prod *= arr[i] ? 1 : -1
  }
  return sum
}

