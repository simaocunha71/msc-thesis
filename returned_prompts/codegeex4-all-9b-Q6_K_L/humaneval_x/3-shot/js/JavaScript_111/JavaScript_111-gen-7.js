  var result = {};
  var list = test.split(' ');
  var max = 0;
  for (const item of list) {
    var count = 0;
    for (const item2 of list) {
      if (item == item2) {
        count += 1;
      }
    }
    if (count > max) {
      max = count;
    }
  }
  for (const item of list) {
    var count = 0;
    for (const item2 of list) {
      if (item == item2) {
        count += 1;
      }
    }
    if (count == max) {
      result[item] = count;
    }
  }
  return result;
}