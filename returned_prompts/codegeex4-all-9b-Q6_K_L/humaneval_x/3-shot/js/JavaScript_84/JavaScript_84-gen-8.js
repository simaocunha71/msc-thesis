  let sum = 0;
  let binary = N.toString(2);
  for (const c of binary) {
    sum += parseInt(c);
  }
  return sum.toString(2);
}



