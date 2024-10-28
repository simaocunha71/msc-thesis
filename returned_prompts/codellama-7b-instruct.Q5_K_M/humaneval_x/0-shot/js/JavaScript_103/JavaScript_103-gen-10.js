/*
1. Compute the average of the integers from n through m.
2. Round the average to the nearest integer.
3. Convert the rounded integer to binary.
4. If n is greater than m, return -1.
*/


  // 1. Compute the average of the integers from n through m.
  const total = m - n + 1;
  const average = total / 2;

  // 2. Round the average to the nearest integer.
  const rounded = Math.round(average);

  // 3. Convert the rounded integer to binary.
  const binary = (rounded >>> 0).toString(2);

  // 4. If n is greater than m, return -1.
  if (n > m) return -1;

  return `0b${binary}`;
}


