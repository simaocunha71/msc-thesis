  let mean = numbers.reduce((sum, val) => sum + val, 0) / numbers.length;
  let sum = numbers.reduce((sum, val) => sum + Math.abs(val - mean), 0);
  return sum / numbers.length;
}



