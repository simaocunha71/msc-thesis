  for  (let i  in b)  {
    if  (a.includes(b))  {
      return true;
    }
    b = b.slice(1) + b[0];
  }
  return false;
}



