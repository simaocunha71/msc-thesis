  let num_dict = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9
  };

  let sorted_numbers = Object.keys(num_dict).sort((a, b) => num_dict[a] - num_dict[b]);
  let result = sorted_numbers.filter(x => numbers.includes(x)).join(' ');
  return result;
} 



