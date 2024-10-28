  var result = [];
  for (const v of values) {
    if (Number.isInteger(v)) {
      result.push(v);
    }
  }
  return result;
}



