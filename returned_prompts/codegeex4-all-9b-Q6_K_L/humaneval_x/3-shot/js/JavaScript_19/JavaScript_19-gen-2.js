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

  const words = numbers.split(' ');
  const numbers_array = words.map(word => number_map[word]);
  numbers_array.sort((a, b) => a - b);

  return numbers_array.map(number => Object.keys(number_map)[number]).join(' ');
}