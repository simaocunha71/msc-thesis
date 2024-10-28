  var result = l;

  for (let i = 0; i < l.length; i += 2) {
    if (i + 1 < l.length) {
      if (l[i] > l[i + 1]) {
        result[i] = l[i + 1];
        result[i + 1] = l[i];
      }
    }
  }

  return result;
}



