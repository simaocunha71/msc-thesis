  var dict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
  }

  var numbers = numbers.split(' ');
  numbers = numbers.sort((a, b) => dict[a] - dict[b]);
  return numbers.join(' ');
}



