  let inc = true;
  let dec = true;
  for (let i = 0; i < l.length - 1; i++) {
    if (l[i] > l[i + 1]) {
      inc = false;
    }
    if (l[i] < l[i + 1]) {
      dec = false;
    }
  }
  return inc || dec;
}



