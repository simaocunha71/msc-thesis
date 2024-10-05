  let total = number;
  let left = remaining;
  
  if (need < remaining) {
    total += need;
    left -= need;
  } else {
    total += remaining;
    left = 0;
  }
  
  return [total, left];
}



