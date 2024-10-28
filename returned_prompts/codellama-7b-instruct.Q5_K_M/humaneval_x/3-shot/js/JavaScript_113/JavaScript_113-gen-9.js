  var result = [];
  for (let i = 0; i < lst.length; i++) {
    var count = 0;
    for (let c of lst[i]) {
      if (c % 2 != 0) {
        count += 1;
      }
    }
    result.push(count);
  }
  return result;
}



