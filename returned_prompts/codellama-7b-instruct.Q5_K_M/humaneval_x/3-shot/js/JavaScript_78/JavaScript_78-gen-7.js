  var count = 0;
  var numbers = num.split('');
  var hex_to_decimal = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
  }

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] >= 'A' && numbers[i] <= 'F') {
      count += 1;
    }
  }

  return count;
}



