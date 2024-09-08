  let inc = true;
  for (let i = 0; i < l.length - 1; i++) {
    if (l[i] > l[i + 1]) {
      inc = false;
      break;
    }
  }
  if (inc) {
    return true;
  }
  inc = true;
  for (let i = 0; i < l.length - 1; i++) {
    if (l[i] < l[i + 1]) {
      inc = false;
      break;
    }
  }
  return inc;
}



