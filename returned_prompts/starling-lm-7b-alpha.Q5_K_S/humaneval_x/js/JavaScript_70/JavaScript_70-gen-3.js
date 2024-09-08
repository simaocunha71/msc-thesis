  let result = [];
  let remaining = lst.slice();

  while (remaining.length > 0) {
    result.push(Math.min(...remaining));
    remaining = remaining.filter(x => x !== Math.max(...remaining));
  }

  return result;
}



