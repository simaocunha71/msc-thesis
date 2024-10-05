  var result = [n];
  var next_number = n + 1;

  if (n % 2 == 0) {
    next_number += 1;
  }

  for (let i = 0; i < n - 1; i++) {
    result.push(next_number);
    next_number += 2;
  }

  return result;
}