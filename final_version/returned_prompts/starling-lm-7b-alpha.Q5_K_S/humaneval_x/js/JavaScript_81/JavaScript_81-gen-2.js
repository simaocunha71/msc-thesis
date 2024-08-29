  const letter_grades = {
    'A+': { 'min': 4.0, 'max': Infinity },
    'A-': { 'min': 3.7, 'max': 3.2999999999999996 },
    'B+': { 'min': 3.0, 'max': 2.6999999999999998 },
    'B-': { 'min': 2.3, 'max': 2.2999999999999998 },
    'C+': { 'min': 1.7, 'max': 1.6999999999999998 },
    'C-': { 'min': 1.3, 'max': 1.2999999999999998 },
    'D+': { 'min': 0.7, 'max': 0.6999999999999998 },
    'D-': { 'min': 0.0, 'max': 0.6999999999999998 },
    'E' : { 'min': 0.0, 'max': 0.0 }
  }

  const result = [];

  for (const grade of grades) {
    let min = Infinity;
    let max = -Infinity;
    for (const key in letter_grades) {
      min = Math.min(min, letter_grades[key]['min']);
      max = Math.max(max, letter_grades[key]['max']);
    }
    if (min <= grade && grade <= max) {
      result.push(key);
    } else {
      result.push('F');
    }
  }

  return result;
}



