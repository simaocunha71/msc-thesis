  let eaten = Math.min(remaining, need);
  let left = remaining - eaten;
  return [number + eaten, left];
}