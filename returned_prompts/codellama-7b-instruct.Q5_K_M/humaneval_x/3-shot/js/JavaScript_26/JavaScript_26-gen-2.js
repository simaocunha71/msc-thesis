  var result = [];
  var seen = {};

  for (const n of numbers) {
    if (!(n in seen)) {
      seen[n] = true;
      result.push(n);
    }
  }

  return result;
}



