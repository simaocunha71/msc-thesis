  lst.sort((a, b) => a - b);
  let result = [];
  while (lst.length) {
    result.push(lst.shift()); // take the smallest
    if (lst.length) {
      result.push(lst.pop()); // take the largest
    }
  }
  return result;
}



