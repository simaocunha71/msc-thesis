  var result = [];

  for (let i = 0; i < lst.length; i++) {
    var count = 0;
    for (const c of lst[i]) {
      if (c % 2 != 0) {
        count += 1;
      }
    }
    result.push(`the number of odd elements ${count}n the str${count}ng ${i} of the ${i}nput.`);
  }

  return result;
}



