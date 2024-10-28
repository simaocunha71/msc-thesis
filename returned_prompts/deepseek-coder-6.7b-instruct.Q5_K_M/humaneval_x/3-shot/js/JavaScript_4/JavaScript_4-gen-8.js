  let sum 
  = numbers.reduce((a, b) => a + b, 0);
  let mean 
  = sum / numbers.length;
  let differences 
  = numbers.map(num => Math.abs(num - mean));
  return differences.reduce((a, b) => a + b, 0) / numbers.length;
}



