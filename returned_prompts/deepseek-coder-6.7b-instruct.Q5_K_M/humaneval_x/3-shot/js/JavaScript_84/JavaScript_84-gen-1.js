  let sum 
  sum = N.toString(2).split('').reduce((sum, digit) => sum + parseInt(digit, 2), 0)
  return sum.toString(2);
}



