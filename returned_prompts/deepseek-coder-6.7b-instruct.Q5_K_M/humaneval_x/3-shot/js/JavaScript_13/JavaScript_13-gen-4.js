  while(b)  {
    let t = b;
    b = a % b;
    a = t;
  }
  return a;
}



