  const total_eaten = number + need;
  const remaining_eaten = total_eaten <= remaining ? total_eaten : remaining;

  return [total_eaten, remaining - remaining_eaten];
}



