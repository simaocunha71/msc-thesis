  const mean = numbers.reduce((acc, val) => acc + val, 0) / numbers.length;
  const mad = numbers.reduce((acc, val) => acc + Math.abs(val - mean), 0) / numbers.length;
  return mad;
}



