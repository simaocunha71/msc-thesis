  let evens = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      evens.push(l[i]);
    }
  }
  evens.sort((a, b) => a - b);
  let result = [];
  let even_index = 0;
  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      result.push(evens[even_index]);
      even_index += 1;
    } else {
      result.push(l[i]);
    }
  }
  return result;
}

