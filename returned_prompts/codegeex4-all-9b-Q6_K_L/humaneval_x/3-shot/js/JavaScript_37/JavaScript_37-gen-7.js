  var even_indices = [];
  var odd_indices = [];

  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      even_indices.push(l[i]);
    } else {
      odd_indices.push(l[i]);
    }
  }

  even_indices.sort((a, b) => a - b);

  var result = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      result.push(even_indices[Math.floor(i / 2)]);
    } else {
      result.push(odd_indices[Math.floor(i / 2)]);
    }
  }

  return result;
}



