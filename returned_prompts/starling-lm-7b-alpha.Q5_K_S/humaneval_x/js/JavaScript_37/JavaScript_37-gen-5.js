  let result = [...l];
  let even_index = 0;
  while (even_index < l.length) {
    result[2 * even_index] = l[2 * even_index];
    even_index += 1;
  }
  result = result.sort((a, b) => a - b);
  return result;
}



