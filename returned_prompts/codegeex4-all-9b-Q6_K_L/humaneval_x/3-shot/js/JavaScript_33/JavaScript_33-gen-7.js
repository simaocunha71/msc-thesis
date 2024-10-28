  var third_indices = [];
  for (let i = 0; i < l.length; i += 3) {
    third_indices.push(l[i]);
  }
  third_indices.sort();

  for (let i = 0; i < l.length; i += 3) {
    l[i] = third_indices[i / 3];
  }

  return l;
}

