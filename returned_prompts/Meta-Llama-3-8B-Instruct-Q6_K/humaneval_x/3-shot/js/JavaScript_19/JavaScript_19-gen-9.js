  let num_dict = {
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

  let nums = numbers.split(' ');
  nums.sort((a, b) => {
    return num_dict[a] - num_dict[b];
  });

  return nums.join(' ');
}