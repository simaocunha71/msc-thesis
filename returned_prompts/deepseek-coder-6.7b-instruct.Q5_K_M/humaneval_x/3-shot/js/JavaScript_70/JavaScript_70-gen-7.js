  lst.sort((a, b) => a - b);
  let result = [];
  while (lst.length) {
    result.push(lst.shift()); // remove and push min
    if (lst.length) {
      result.push(lst.pop()); // remove and push max
    }
  }
  return result;
}



