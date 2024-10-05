  let eaten = number + need - remaining;
  if (eaten > remaining) {
    eaten -= remaining;
    remaining = 0;
  } else {
    remaining -= eaten;
  }
  return [number + need, remaining];
}