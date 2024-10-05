  a = a.toString().replace(",", ".");
  b = b.toString().replace(",", ".");

  if(a > b) return a;
  if(b > a) return b;
  return null;
}



