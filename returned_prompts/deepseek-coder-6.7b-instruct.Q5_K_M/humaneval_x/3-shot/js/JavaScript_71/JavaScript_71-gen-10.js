  if (a + b <= c || a + c <= b || b + c <= a) 
    return -1;
  else {
    let s = (a + b + c) / 2;
    return Number((Math.sqrt(s * (s - a) * (s - b) * (s - c))).toFixed(2));
  }
}



