  let totalCarrots = number;
  if(need <= remaining) {
    totalCarrots += need;
    remaining -= need;
  } else {
    totalCarrots += remaining;
    remaining = 0;
  }
  return [totalCarrots, remaining];
}



