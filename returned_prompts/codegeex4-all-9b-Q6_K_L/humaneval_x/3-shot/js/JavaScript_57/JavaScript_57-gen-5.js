  var increasing = l[1] > l[0];
  for (let i = 1; i < l.length; i++) {
    if ((l[i] > l[i-1]) != increasing) {
      return false;
    }
  }
  return true;
}