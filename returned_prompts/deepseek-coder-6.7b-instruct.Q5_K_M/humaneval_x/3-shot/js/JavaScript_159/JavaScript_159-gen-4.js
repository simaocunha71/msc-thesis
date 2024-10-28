  let total = number;
  let eaten = 0;
  
  if (need <= remaining){
      eaten = need;
      remaining -= need;
  } else {
      eaten = remaining;
      remaining = 0;
  }
  
  total += eaten;
  return [total, remaining];
}



