  let total_eaten = number;
  let eaten = Math.min(remaining - number, need - number);
  total_eaten += eaten;
  remaining -= eaten;
  need -= eaten;

  return [total_eaten, remaining];
}



