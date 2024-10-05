  let result = [];
  let current_factor = 2;
  while (n > 1) {
    let count = 0;
    while (n % current_factor == 0) {
      n /= current_factor;
      count++;
    }
    if (count > 0) {
      for (let i = 0; i < count; i++) {
        result.push(current_factor);
      }
    }
    current_factor++;
  }
  return result;
}