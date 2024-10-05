  const number_map = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
  };

  const numbers = numbers.split(' ');

  numbers.sort((a, b) => {
    return number_map[a] - number_map[b];
  });

  return numbers.join(' ');
}



