/*
  First, make a function that takes the operator and operand as input and returns the 
  expression in string form.

  */
  const toExpression = (operator, operand) => {
    return operand.join(` ${operator} `)
  }

B:
/*
  Next, make a function that takes the expression as string form and returns its 
  evaluation.

  */
  const evaluate = (expression) => {
    return eval(expression)
  }

C:
/*
  Use the two functions to build the final result.

  */
  const result = evaluate(toExpression(operator, operand))

  return result
}

const operator = ['+', '*', '-']
const operand = [2, 3, 4, 5]

console.log(doAlgebra(operator, operand))

