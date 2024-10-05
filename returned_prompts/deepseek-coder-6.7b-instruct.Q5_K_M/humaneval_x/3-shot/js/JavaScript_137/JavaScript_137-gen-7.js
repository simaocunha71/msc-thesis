  a = (typeof a == "string") ? parseFloat(a.replace(",", ".")) : a;
  b = (typeof b == "string") ? parseFloat(b.replace(",", ".")) : b;

  return (a > b) ? a : ((a < b) ? b : null);
}



