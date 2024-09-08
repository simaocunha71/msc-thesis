  let result = [];
  let min = Infinity;
  let max = -Infinity;
  for (const num of lst) {
    if (num < 0) {
      if (num > max) {
        max = num;
      }
    } else if (num > 0) {
      if (num < min) {
        min = num;
      }
    }
  }
  if (min == Infinity) {
    result.push(null);
  } else {
    result.push(min);
  }
  if (max == -Infinity) {
    result.push(null);
  } else {
    result.push(max);
  }
  return result;
}



