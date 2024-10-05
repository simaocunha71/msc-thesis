  a = Math.abs(a);
  b = Math.abs(b);
  while  (a >= 10)  {
    a  /= 10;
  }
  while  (b >= 10)  {
    b  /= 10;
  }
  return Math.floor(a) * Math.floor(b);
}


