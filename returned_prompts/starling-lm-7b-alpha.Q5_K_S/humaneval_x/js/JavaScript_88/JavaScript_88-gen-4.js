  let result = [...array];

  let sum = result[0] + result[result.length - 1];

  if (sum % 2 == 0) {
    result.sort((a, b) => b - a);
  } else {
    result.sort((a, b) => a - b);
  }

  return result;
}



