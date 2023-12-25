/*
  Given two lists operator, and operand. The first list has basic algebra operations, and 
  the second list is a list of integers. Use the two given lists to build the algebric 
  expression and return the evaluation of this expression.

  The basic algebra operations:
  Addition ( + ) 
  Subtraction ( - ) 
  Multiplication ( * ) 
  Floor division ( // ) 
  Exponentiation ( ** ) 

  Example:
  operator['+', '*', '-']
  array = [2, 3, 4, 5]
  result = 2 + 3 * 4 - 5
  => result = 9

  Note:
      The length of operator list is equal to the length of operand list minus one.
      Operand is a list of of non-negative integers.
      Operator list has at least one operator, and operand list has at least two operands.

  */
const doAlgebra = (operator, operand) => {
    let tempArray = [];
    for (let i=0; i<operand.length-1; i++){
        if(Math.abs(operand[i])>6){
            tempArray.push('floor');
            break;
        }else{
            tempArray.push(Math.round(operand[i]));
        }
    };
    let operatorList = [];
    for (let i=0; i<operator.length-1; i++){
        if(!tempArray[i]){
            break;
        }else{
            operatorList.push(...tempArray[i]);
        }
    };
    
    let result = 0;
    for (let i=0; i<operatorList.length-1; i++){
        if(operatorList[i]==='floor'){
            const tempVal = parseInt(result)+parseInt(operatorList[i+1]);
            const modulus = Math.abs(parseInt(operatorList[i]));
            result += (tempVal % modulus);
        }else{
            // push to new array
            for (let j=0; j<parseInt(operatorList[i]).