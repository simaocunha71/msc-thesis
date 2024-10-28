  var result = [];

  for (var i = 0; i < grades.length; i++) {
    if (grades[i] >= 4.0) {
      result.push("A+");
    } else if (grades[i] >= 3.7) {
      result.push("A");
    } else if (grades[i] >= 3.3) {
      result.push("A-");
    } else if (grades[i] >= 3.0) {
      result.push("B+");
    } else if (grades[i] >= 2.7) {
      result.push("B");
    } else if (grades[i] >= 2.3) {
      result.push("B-");
    } else if (grades[i] >= 2.0) {
      result.push("C+");
    } else if (grades[i] >= 1.7) {
      result.push("C");
    } else if (grades[i] >= 1.3) {
      result.push("C-");
    } else if (grades[i] >= 1.0) {
      result.push("D+");
    } else if (grades[i] >= 0.7) {
      result.push("D");
    } else if (grades[i] >= 0.0) {
      result.push("D-");
    } else {
      result.push("E");
    }
  }

  return result;
}



