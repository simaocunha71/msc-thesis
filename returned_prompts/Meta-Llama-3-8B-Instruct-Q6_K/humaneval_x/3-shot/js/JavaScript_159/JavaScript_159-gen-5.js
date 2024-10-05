  let total_eaten = number + (need - remaining);
  let carrots_left = total_eaten - need;
  return [total_eaten, carrots_left];
}