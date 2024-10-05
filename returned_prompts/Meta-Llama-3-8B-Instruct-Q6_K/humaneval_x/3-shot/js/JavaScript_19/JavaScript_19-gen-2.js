  const num_map = {
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

  const num_list = numbers.split(' ');
  const sorted_list = num_list.slice().sort((a, b) => num_map[a] - num_map[b]);

  return sorted_list.join(' ');
}