/*
  * Your code here
  * Remember to use the value parameter in your function
  */
  const val = parseFloat(value);
  const round = Math.round(val);

  if (Math.abs(val - round) === Math.abs(val - Math.round(val - 1))) return Math.round(val - 1);
  return round;
}
