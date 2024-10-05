  let maxSoFar = numbers[0];
  let maxUntilNow = [numbers[0]];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > maxSoFar) {
      maxSoFar = numbers[i];
    }
    maxUntilNow.push(maxSoFar);
  }
  return maxUntilNow;
}