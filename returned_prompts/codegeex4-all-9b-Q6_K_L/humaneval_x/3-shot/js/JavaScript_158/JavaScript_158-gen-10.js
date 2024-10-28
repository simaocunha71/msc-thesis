  var maxCount = 0;
  var result = "";
  for (const word of words) {
    var count = {};
    for (const c of word) {
      if (count[c] == undefined) {
        count[c] = 1;
      } else {
        count[c] += 1;
      }
    }
    if (Object.keys(count).length > maxCount) {
      maxCount = Object.keys(count).length;
      result = word;
    }
  }
  return result;
}