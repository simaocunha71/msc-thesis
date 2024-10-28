
  // Check if the length of the operand list is correct
  const operandLength = operand.length;
  if (operator.length !== operandLength - 1) {
    console.log("Error: The length of the operator list is not equal to the length of the operand list minus one.");
    return;
  }

  // Check if the operand list has at least two elements
  if (operandLength < 2) {
    console.log("Error: The length of the operand list is less than 2.");
    return;
  }

  // Check if all elements in the operand list are non-negative integers
  for (let i = 0; i < operandLength; i++) {
    if (typeof operand[i] !== "number" || operand[i] < 0 || operand[i] % 1 !== 0) {
      console.log("Error: All elements in the operand list should be non-negative integers.");
      return;
    }
  }

  // Check if the operator list has at least one operator
  if (operator.length < 1) {
    console.log("Error: The length of the operator list is less than 1.");
    return;
  }

  // Check if all elements in the operator list are valid operators
  for (let i = 0; i < operator.length; i++) {
    if (operator[i] !== "+" && operator[i] !== "-" && operator[i] !== "*" && operator[i] !== "//" && operator[i] !== "**") {
      console.log("Error: All elements in the operator list should be valid operators.");
      return;
    }
  }

  // Evaluate the expression
  let result = operand[0];
  for (let i = 1; i < operandLength; i++) {
    if (operator[i - 1] === "+") {
      result += operand[i];
    } else if (operator[i - 1] === "-") {
      result -= operand[i];
    } else if (operator[i - 1] === "*") {
      result *= operand