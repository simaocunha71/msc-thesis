  lst.sort((a, b) => a - b);
  let result = [];
  while (lst.length) {
    result.push(lst.shift()); // Take smallest
    if (lst.length) {
      result.push(lst.pop()); // Take largest
    }
  }
  return result;
}



