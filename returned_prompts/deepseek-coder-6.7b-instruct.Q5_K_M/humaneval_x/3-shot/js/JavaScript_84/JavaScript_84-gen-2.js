  let binary = (N >>> 0).toString(2);
  let sum = 0;
  for (let i = 0; i < binary.length; i++) {
    sum += parseInt(binary[i]);
  }
  return sum.toString(2);
}



