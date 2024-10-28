  var evenIndicies = [];

  for (let i = 0; i < l.length; i += 2) {
    evenIndicies.push(l[i]);
  }

  evenIndicies.sort((a, b) => a - b);

  for (let i = 0; i < evenIndicies.length; i += 2) {
    l[i] = evenIndicies[i];
  }

  return l;
}