  var result = "";
  for (const group of s.split("")) {
    if (group.length == 2) {
      result += group[0] + group[1];
    } else {
      result += group;
    }
  }
  return result;
}