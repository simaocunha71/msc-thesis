  if  (n === 1)  {
    return x === n;
  }

  while  (x % n === 0)  {
    x /= n;
  }

  return x === 1;
}



