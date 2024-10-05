  var result = [];
  for (const g of grades) {
    if (g >= 4.0) {
      result.push('A+');
    } else if (g > 3.7) {
      result.push('A');
    } else if (g > 3.3) {
      result.push('A-');
    } else if (g > 3.0) {
      result.push('B+');
    } else if (g > 2.7) {
      result.push('B');
    } else if (g > 2.3) {
      result.push('B-');
    } else if (g > 2.0) {
      result.push('C+');
    } else if (g > 1.7) {
      result.push('C');
    } else if (g > 1.3) {
      result.push('C-');
    } else if (g > 1.0) {
      result.push('D+');
    } else if (g > 0.7) {
      result.push('D');
    } else if (g > 0.0) {
      result.push('D-');
    } else {
      result.push('E');
    }
  }
  return result;
}