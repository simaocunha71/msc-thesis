  let expression = []
  for (let i = 0; i < operator.length; i++) {
    expression.push(`${operand[i]} ${operator[i]}`)
  }
  expression.push(`${operand[operand.length - 1]}`)
  return eval(expression.join(' '))
}


