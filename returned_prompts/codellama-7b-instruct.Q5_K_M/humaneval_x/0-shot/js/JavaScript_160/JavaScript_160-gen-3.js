  const expression = operand.reduce((acc, curr, i, arr) => {
    if (i === 0) {
      return `${curr}`
    } else {
      const op = operator[i - 1]
      return `${acc} ${op} ${curr}`
    }
  })
  return eval(expression)
}


console.log(doAlgebra(['+', '*', '-'], [2, 3, 4, 5])) // 9
console.log(doAlgebra(['+', '-'], [2, 3, 4, 5])) // 1
console.log(doAlgebra(['+', '-', '*'], [2, 3, 4, 5])) // 3
console.log(doAlgebra(['+', '-', '*', '/'], [2, 3, 4, 5])) // 3
console.log(doAlgebra(['+', '-', '*', '/', '**'], [2, 3, 4, 5])) // 3
console.log(doAlgebra(['+', '-', '*', '/', '**', '%'], [2, 3, 4, 5])) // 3
console.log(doAlgebra(['+', '-', '*', '/', '**', '%', '<<'], [2, 3, 4, 5])) // 3
console.log(doAlgebra(['+', '-', '*', '/', '**', '%', '<<', '>>'], [2, 3, 4, 5])) // 3
console.log(doAlgebra(['+', '-', '*', '/', '**', '%', '<<', '>>', '&'], [2, 3, 4, 5])) // 3
console.log(doAlgebra(['+', '-', '*', '/', '**', '%', '<<', '>>', '&', '^'], [2, 3, 4, 5])) // 3
console.log(doAlgebra(['+', '-', '*', '/', '**', '%', '<<', '>>', '&', '^', '|'], [2, 3, 4, 5]))