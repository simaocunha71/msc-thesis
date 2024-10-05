  var result = [];
  var odd_count = 0;

  for (const c of lst) {
    for (const digit of c) {
      if (digit % 2 != 0) {
        odd_count += 1;
      }
    }
    result.push("the number of odd elements " + odd_count + "n the str" +
      odd_count + "ng " + odd_count + " of the " + odd_count + "nput.");
    odd_count = 0;
  }

  return result;
}



