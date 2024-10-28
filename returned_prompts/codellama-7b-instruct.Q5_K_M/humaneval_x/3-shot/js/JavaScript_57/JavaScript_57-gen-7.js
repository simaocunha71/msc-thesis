  let inc = true;

  for (let i = 1; i < l.length; i++) {
    if (l[i] > l[i-1]) {
      inc = true;
    } else if (l[i] < l[i-1]) {
      inc = false;
    } else {
      return false;
    }
  }

  return inc;
}



