  const number_to_int = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9};
  const int_to_number = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'};
  const numbers_list = numbers.split(' ');

  numbers_list.sort((a, b) => number_to_int[a] - number_to_int[b]);

  return numbers_list.join(' ');
}