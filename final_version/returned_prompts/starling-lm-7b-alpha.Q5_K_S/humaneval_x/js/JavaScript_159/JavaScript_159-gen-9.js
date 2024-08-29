  let total = number + need;
  if (total > remaining) {
    total = remaining;
  }

  return [total, remaining - total];
}



