  let max_so_far = Number.NEGATIVE_INFINITY;
  let result = [];

  for (let i = 0; i < numbers.length; i++) {
    max_so_far = Math.max(max_so_far, numbers[i]);
    result.push(max_so_far);
  }

  return result;
}



