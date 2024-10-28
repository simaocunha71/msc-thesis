  if (arr.length == 0) {
    return null;
  }
  let result = 0;
  for (const i of arr) {
    result += i;
  }
  return result;
}