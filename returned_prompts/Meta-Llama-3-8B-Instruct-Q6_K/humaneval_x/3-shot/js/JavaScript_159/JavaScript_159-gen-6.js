  let totalEaten = number + Math.min(need, remaining);
  let carrotsLeft = remaining - (need - totalEaten);
  return [totalEaten, carrotsLeft];
}