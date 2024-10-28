  if (arr.length == 0) return null;
  let result = 1;
  for (let num of arr) {
    if (num < 0) result *= -1;
    else if (num > 0) result *= 1;
    else result *= 0;
  }
  return result;
}



