  let even_indices = [];
  for (let i = 0; i < l.length; i += 2) {
    even_indices.push(l[i]);
  }
  even_indices.sort((a, b) => a - b);
  for (let i = 0; i < even_indices.length; i++) {
    l[i * 2] = even_indices[i];
  }
  return l;
}



