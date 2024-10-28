  let counter = 0;

  for (const char of num) {
    if (char === 'A' || char === 'B' || char === 'D' || char === 'E' || char === 'F') {
      counter++;
    }
  }

  return counter;
}



