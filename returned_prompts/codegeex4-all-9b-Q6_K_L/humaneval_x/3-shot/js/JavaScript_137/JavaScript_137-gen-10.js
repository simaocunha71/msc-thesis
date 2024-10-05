  if (a === b) {
    return null;
  }
  var aFloat = parseFloat(a);
  var bFloat = parseFloat(b);
  if (isNaN(aFloat) || isNaN(bFloat)) {
    return aFloat > bFloat ? a : b;
  }
  return aFloat > bFloat ? aFloat : bFloat;
}



