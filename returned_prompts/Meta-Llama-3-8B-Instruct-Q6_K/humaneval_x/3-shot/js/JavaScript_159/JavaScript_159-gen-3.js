  let eaten = number + need;
  let left = remaining - (need - eaten);
  return [eaten, left];
}