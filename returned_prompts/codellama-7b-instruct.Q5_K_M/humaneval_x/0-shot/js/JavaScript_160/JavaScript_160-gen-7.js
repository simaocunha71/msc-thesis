  const expression = operand.reduce((acc, cur, idx, arr) => {
    if (idx === 0) {
      acc = `${cur}`
    } else if (idx === arr.length - 1) {
      acc = `${acc} ${operator[idx - 1]} ${cur}`
    } else {
      acc = `${acc} ${operator[idx - 1]} ${cur}`
    }
    return acc
  }, '')
  console.log(expression)
  return eval(expression)
}

console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5]))
