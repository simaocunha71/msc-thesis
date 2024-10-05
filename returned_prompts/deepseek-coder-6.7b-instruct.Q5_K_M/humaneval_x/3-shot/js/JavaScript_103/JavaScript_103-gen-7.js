  if  (n > m)  {
    return -1;
  } 
  let avg = Math.round((n + m) / 2);
  return (avg >>> 0).toString(2);
}



