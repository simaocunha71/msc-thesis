/*
  * 1. Find the largest prime number in the list
  * 2. Return the sum of its digits
*/

function isPrime(num) {
  if (num <= 1) return false
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false
  }
  return true
}

let max = 0
let primeSum = 0

for (let i = 0; i < lst.length; i++) {
  if (lst[i] > max && isPrime(lst[i])) {
    max = lst[i]
    primeSum = 0
  }
  primeSum += lst[i]
}

return primeSum
}
