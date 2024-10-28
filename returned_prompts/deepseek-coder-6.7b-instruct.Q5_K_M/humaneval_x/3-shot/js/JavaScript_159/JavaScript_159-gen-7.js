  let total = number;
  let eaten = number;

  if  (need  - eaten < remaining)  {
    total += need  - eaten;
    remaining -= need  - eaten;
  }  else  {
    total += remaining;
    remaining = 0;
  }

  return [total, remaining];
}



