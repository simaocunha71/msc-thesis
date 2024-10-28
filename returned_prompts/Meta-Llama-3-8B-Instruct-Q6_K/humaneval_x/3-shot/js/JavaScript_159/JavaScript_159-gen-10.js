  let eaten = number + Math.min(need, remaining);
  let left = remaining - (need - eaten);
  return [eaten, left];
}