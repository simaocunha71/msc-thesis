  let inc = true;
  let dec = true;
  for (let i = 1; i < l.length; i++) {
    inc &= l[i] >= l[i-1];
    dec &= l[i] <= l[i-1];
  }
  return inc || dec;
}



