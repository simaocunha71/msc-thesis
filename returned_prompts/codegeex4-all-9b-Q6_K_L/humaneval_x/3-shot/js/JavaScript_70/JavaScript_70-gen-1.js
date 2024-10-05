  let result = [];
  let current = lst.slice();

  while (current.length > 0) {
    result.push(Math.min(...current));
    current = current.filter(x => x != Math.min(...current));
    if (current.length > 0) {
      result.push(Math.max(...current));
      current = current.filter(x => x != Math.max(...current));
    }
  }

  return result;
}

