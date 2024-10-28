  if (a == b) return null;
  if (typeof a == 'string') a = a.replace(',', '.');
  if (typeof b == 'string') b = b.replace(',', '.');
  if (a < b) return b;
  return a;
}



