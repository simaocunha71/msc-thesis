const uniqueDigits = (x) => {
  const isEven = (n) => n % 2 === 0
  const isOdd = (n) => n % 2 !== 0
  return x.filter(isOdd).sort((a, b) => a - b)
}
