  const fib_matrix = [[0, 0, 2, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]];
  const result = fib_matrix[n % 4];

  return result[0] + result[1] + result[2] + result[3];
}



