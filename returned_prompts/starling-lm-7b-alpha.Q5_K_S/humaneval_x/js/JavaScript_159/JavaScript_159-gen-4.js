  let eaten = Math.min(remaining, need - number);
  return [number + eaten, remaining - eaten];
}



