  a = Number(a.toString().replace(/,/g, '.'));
  b = Number(b.toString().replace(/,/g, '.'));

  if  (a  != b)  {
    return Math.max(a, b);
  }
  return null;
}



