  return N.toString(2).split('').reduce((a, b) => +a + +b)

B:
  return N.toString(2).split('').reduce((a, b) => a + b)

C:
  return (N.toString(2).split('').reduce((a, b) => a + b))

D:
  return parseInt(N.toString(2).split('').reduce((a, b) => a + b))
}
