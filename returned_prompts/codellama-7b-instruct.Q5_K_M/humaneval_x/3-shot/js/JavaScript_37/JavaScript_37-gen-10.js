  var result = l.slice();

  for (let i = 0; i < l.length; i += 2) {
    result[i] = l[i];
  }

  result.sort();

  return result;
}



