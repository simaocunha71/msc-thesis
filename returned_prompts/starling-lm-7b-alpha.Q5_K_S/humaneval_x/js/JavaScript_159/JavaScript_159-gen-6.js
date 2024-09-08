  const eaten = number + Math.min(remaining, need);
  const left = remaining - Math.min(remaining, need);
  return [eaten, left];
}



