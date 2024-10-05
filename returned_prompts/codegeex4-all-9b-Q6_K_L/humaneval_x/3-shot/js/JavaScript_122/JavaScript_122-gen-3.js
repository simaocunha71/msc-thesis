  var sum = 0;
  for (let i = 0; i < k; i++) {
    let current = arr[i];
    while (current >= 10) {
      current = current % 10;
    }
    sum += current;
  }
  return sum;
}