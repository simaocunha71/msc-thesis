  if  (a === b) {
    return null;
  }

  if  (typeof a  === 'string')  {
    a = parseFloat(a.replace(',', '.'));
  }

  if  (typeof b  === 'string')  {
    b = parseFloat(b.replace(',', '.'));
  }

  return  a > b  ?  a  :  b;
}



