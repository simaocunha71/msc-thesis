  var third_indices = [];
  var third_values = [];

  for (var i = 0; i < l.length; i++) {
    if (i % 3 == 2) {
      third_indices.push(i);
      third_values.push(l[i]);
    }
  }

  third_values.sort((a, b) => a - b);

  for (var i = 0; i < third_indices.length; i++) {
    l[third_indices[i]] = third_values[i];
  }

  return l;
}