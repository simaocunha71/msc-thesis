  lst.sort((a, b) => a - b);
  const result = [];
  while (lst.length) {
    result.push(lst.shift()); // take smallest
    if (lst.length) {
      result.push(lst.pop()); // take largest
    }
  }
  return result;
}



