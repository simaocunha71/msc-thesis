  lst.sort((a, b) => a - b);
  let result = [];
  while (lst.length) {
    result.push(lst.shift()); // Take minimum
    if (lst.length) {
      result.push(lst.pop()); // Then maximum
    }
  }
  return result;
}



