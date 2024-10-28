  if (arr.length === 0) {
    return true;
  }
  let sorted = [...arr].sort((a, b) => a - b);
  let operations = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== sorted[i]) {
      operations++;
    }
  }
  return operations <= Math.floor(arr.length / 2);
}