  let mean = numbers.reduce((a, b) => a + b) / numbers.length;
  let deviation = numbers.map((x) => Math.abs(x - mean));
  return deviation.reduce((a, b) => a + b) / numbers.length;
}



