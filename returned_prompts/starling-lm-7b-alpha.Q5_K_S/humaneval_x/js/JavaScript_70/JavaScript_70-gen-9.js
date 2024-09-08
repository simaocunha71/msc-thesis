  let result = [];
  let remaining = lst.slice();

  while (remaining.length) {
    result.push(Math.min(...remaining));
    remaining = remaining.slice(remaining.indexOf(Math.min(...remaining)) + 1);
    result.push(Math.max(...remaining));
    remaining = remaining.slice(remaining.indexOf(Math.max(...remaining)) + 1);
  }

  return result;
}



