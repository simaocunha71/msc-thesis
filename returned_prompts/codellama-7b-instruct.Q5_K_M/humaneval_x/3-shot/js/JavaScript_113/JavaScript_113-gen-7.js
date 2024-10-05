  var result = [];
  var count = 0;
  for (const str of lst) {
    for (const c of str) {
      if (parseInt(c) % 2 != 0) {
        count++;
      }
    }
    result.push("the number of odd elements " + count + "n the str" + (lst.indexOf(str) + 1) + "ng " + (lst.indexOf(str) + 1) + " of the " + (lst.indexOf(str) + 1) + "nput.");
  }
  return result;
}



