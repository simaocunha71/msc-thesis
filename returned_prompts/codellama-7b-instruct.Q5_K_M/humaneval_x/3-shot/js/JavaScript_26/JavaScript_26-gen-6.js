  let unique_numbers = [];

  for (const n of numbers) {
    if (!unique_numbers.includes(n)) {
      unique_numbers.push(n);
    }
  }

  return unique_numbers;
}



