  let i = 0;
  while (Math.pow(n, i) <= x)  {
    if  (Math.pow(n, i) == x)  {
      return true;
    }
    i++;
  }
  return false;
}



