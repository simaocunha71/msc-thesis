  let sum = arr.reduce((a, b) => a + b, 0);
  let min = Infinity;
  for (let i = 0; i < arr.length; i++) {
    let x = Math.abs(sum - 2 * arr[i]);
    min = Math.min(x, min);
  }
  return min;
}



