  let eaten_carrot = Math.min(need - number, remaining);
  return [number + eaten_carrot, remaining - eaten_carrot];
}



