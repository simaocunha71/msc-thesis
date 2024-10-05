  var result = [];
  for (const s of lst) {
    var cnt = 0;
    for (const c of s) {
      if (parseInt(c) % 2 == 1) {
        cnt += 1;
      }
    }
    result.push(`the number of odd elements ${cnt}n the str${cnt}ng ${cnt} of the ${cnt}nput.`);
  }
  return result;
}



