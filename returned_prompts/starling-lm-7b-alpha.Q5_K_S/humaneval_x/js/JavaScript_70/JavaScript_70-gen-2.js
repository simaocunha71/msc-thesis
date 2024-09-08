  let result = [];
  let remaining = lst.slice();

  while (remaining.length > 0) {
    let min = Math.min(...remaining);
    result.push(min);
    remaining = remaining.filter(x => x != min);
  }

  return result;
}



