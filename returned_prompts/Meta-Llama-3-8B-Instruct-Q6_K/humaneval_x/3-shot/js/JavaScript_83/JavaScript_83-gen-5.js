  let count = 0;
  for (let i = 1; i < 10; i++) {
    count += 1; // start with 1
  }
  for (let i = 1; i < 10; i++) {
    count += Math.pow(10, n - 1); // end with 1
  }
  return count;
}

