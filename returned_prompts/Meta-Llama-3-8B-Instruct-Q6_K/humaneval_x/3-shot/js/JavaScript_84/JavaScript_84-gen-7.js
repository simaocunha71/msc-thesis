  let sum = 0;
  let binary = N.toString(2);
  for (let i = 0; i < binary.length; i++) {
    sum += parseInt(binary[i]);
  }
  return binary;
}