  var result = [];
  var found = {};

  for (const n of numbers) {
    if (!(n in found)) {
      result.push(n);
      found[n] = true;
    }
  }

  return result;
}

