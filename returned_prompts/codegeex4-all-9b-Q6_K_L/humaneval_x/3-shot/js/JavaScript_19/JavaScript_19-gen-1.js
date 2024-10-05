  var number_map = {
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

  var numbers = numbers.split(' ');
  var number_values = [];

  for (const n of numbers) {
    number_values.push(number_map[n]);
  }

  number_values.sort((a, b) => a - b);
  var result = [];

  for (const v of number_values) {
    for (const n in number_map) {
      if (number_map[n] == v) {
        result.push(n);
      }
    }
  }

  return result.join(' ');
}



