  let eaten = number + Math.min(need, remaining);
  let left = remaining - (eaten - number);
  return [eaten, left];
}