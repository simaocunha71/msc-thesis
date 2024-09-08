  let total = number + Math.min(remaining, need);
  remaining -= Math.min(remaining, need);
  need -= Math.min(remaining, need);

  return [total, need];
}



