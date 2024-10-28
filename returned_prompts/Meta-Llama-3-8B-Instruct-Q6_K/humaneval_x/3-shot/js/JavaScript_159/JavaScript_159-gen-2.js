  let eaten = number + need;
  let left = remaining - (need - eaten);
  return [eaten, Math.max(0, left)];
}