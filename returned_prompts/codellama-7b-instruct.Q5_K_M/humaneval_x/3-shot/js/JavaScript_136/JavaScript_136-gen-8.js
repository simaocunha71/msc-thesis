  var smallest = null;
  var largest = null;

  for (var i = 0; i < lst.length; i++) {
    var current = lst[i];
    if (current < 0 && (smallest === null || current < smallest)) {
      smallest = current;
    }
    if (current > 0 && (largest === null || current > largest)) {
      largest = current;
    }
  }

  return [smallest, largest];
}



