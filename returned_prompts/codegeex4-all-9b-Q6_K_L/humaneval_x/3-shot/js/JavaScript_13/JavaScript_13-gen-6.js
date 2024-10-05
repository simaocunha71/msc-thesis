  let greatest = 0;

  for (let i = 1; i <= a && i <= b; i++) {
    if (a % i == 0 && b % i == 0) {
      greatest = i;
    }
  }

  return greatest;
}



