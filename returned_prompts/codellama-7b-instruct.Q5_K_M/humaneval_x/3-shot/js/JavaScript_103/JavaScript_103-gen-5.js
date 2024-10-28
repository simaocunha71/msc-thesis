  if (n > m) return -1;

  // calculate the average
  let sum = (n + m) / 2;
  let rounded = Math.round(sum);

  // convert to binary
  return rounded.toString(2);
}



