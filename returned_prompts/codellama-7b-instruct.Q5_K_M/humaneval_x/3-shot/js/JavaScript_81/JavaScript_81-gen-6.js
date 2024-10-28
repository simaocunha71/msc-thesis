  let result = [];
  let mapping = {
    'A+': 4.0,
    'A': 3.7,
    'A-': 3.3,
    'B+': 3.0,
    'B': 2.7,
    'B-': 2.3,
    'C+': 2.0,
    'C': 1.7,
    'C-': 1.3,
    'D+': 1.0,
    'D': 0.7,
    'D-': 0.0,
    'E': 0.0,
  };

  for (const g of grades) {
    for (const [key, value] of Object.entries(mapping)) {
      if (g >= value) {
        result.push(key);
        break;
      }
    }
  }

  return result;
}



