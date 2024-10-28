  var result = [];
  for (const val of values) {
    if (typeof val == 'number' && Number.isInteger(val)) {
      result.push(val);
    }
  }
  return result;
}



