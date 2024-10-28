  if (numbers.length == 0) {
    return (0, 1);
  } else {
    return (sumProduct(numbers.slice(1), int * numbers[0])[0] + int * numbers[0], sumProduct(numbers.slice(1), int * numbers[0])[1] * numbers[0]);
  }
}



