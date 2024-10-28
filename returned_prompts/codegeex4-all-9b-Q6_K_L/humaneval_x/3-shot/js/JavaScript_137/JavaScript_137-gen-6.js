  var aFloat = parseFloat(a);
  var bFloat = parseFloat(b);
  if (aFloat == bFloat) {
    return null;
  } else if (aFloat > bFloat) {
    return a;
  } else {
    return b;
  }
}



