
const isPrime = (n) => {
  if (n < 2) return false
  const sqrt = Math.sqrt(n)
  for (let i = 2; i <= sqrt; i += 1) {
    if (n % i === 0) return false
  }
  return true
}

let i = 1
let j = 2
let k = 3

while (i < 100) {
  if (isPrime(i) && isPrime(j) && isPrime(k)) {
    if (i * j * k === a) {
      return true
    }
  }
  i += 1
  j += 1
  k += 1
}
return false
}
