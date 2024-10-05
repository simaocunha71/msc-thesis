  const binaryN = N.toString(2);
  const sum = [];
  for (let i = 0; i < binaryN.length; i++) {
    sum.push(binaryN.charAt(i));
  }
  let sumTotal = 0;
  for (let i = 0; i < sum.length; i++) {
    if (sum[i] == 1) {
      sumTotal++;
    }
  }
  return sumTotal;
}
