  var even_indicies = l.filter((_, i) => i % 2 == 0);
  even_indicies.sort((a, b) => a - b);
  var result = [];
  var even_index = 0;
  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      result.push(even_indicies[even_index]);
      even_index += 1;
    } else {
      result.push(l[i]);
    }
  }
  return result;
}