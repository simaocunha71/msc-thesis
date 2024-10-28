  let result = null;
  a = Number(a.toString().replace(',', '.'));
  b = Number(b.toString().replace(',', '.'));

  if(a > b) result = a;
  else if(b > a) result = b;

  return result;
}



