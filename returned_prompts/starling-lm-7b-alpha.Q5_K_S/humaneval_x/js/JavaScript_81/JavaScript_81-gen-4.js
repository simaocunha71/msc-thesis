  const grades_mapping = {
    'A+': { 'min': 4.0, 'max': 4.0 },
    'A': { 'min': 3.7, 'max': 3.7 },
    'A-': { 'min': 3.3, 'max': 3.3 },
    'B+': { 'min': 3.0, 'max': 3.0 },
    'B': { 'min': 2.7, 'max': 2.7 },
    'B-': { 'min': 2.3, 'max': 2.3 },
    'C+': { 'min': 2.0, 'max': 2.0 },
    'C': { 'min': 1.7, 'max': 1.7 },
    'C-': { 'min': 1.3, 'max': 1.3 },
    'D+': { 'min': 1.0, 'max': 1.0 },
    'D': { 'min': 0.7, 'max': 0.7 },
    'D-': { 'min': 0.0, 'max': 0.0 },
    'E': { 'min': 0.0, 'max': 0.0 }
  };

  const result = [];
  for (const gpa of grades) {
    for (const key in grades_mapping) {
      if (grades_mapping[key].min <= gpa && grades_mapping[key].max >= gpa) {
        result.push(key);
        break;
      }
    }
  }

  return result;
}



