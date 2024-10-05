  var result = [];
  for (let str of lst) {
    var count = 0;
    for (let c of str) {
      if (parseInt(c) % 2 == 1) {
        count += 1;
      }
    }
    result.push("the number of odd elements " + count + "n the str" + count + "ng " + count + " of the " + count + "nput.");
  }
  return result;
}

