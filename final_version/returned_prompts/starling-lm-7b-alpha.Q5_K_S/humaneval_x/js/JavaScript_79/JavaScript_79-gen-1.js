  const binary = (decimal >> 1).toString(2);
  const result = ('0' + binary + '0').slice(-8);
  return result;
}



