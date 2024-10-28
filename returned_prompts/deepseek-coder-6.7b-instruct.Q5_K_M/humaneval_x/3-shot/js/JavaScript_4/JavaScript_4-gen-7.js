  let mean = numbers.reduce((a,b) => a + b, 0) / numbers.length;
  return numbers.map(x => Math.abs(x - mean)).reduce((a,b) => a + b, 0) / numbers.length;
}



