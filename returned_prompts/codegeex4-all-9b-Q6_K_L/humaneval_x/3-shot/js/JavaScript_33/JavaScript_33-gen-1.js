  let third_indices = [];
  let third_values = [];

  for (let i = 0; i < l.length; i++) {
    if (i % 3 == 0) {
      third_indices.push(i);
      third_values.push(l[i]);
    }
  }

  third_values.sort((a, b) => {
    return a - b;
  });

  for (let i = 0; i < third_indices.length; i++) {
    l[third_indices[i]] = third_values[i];
  }

  return l;
}