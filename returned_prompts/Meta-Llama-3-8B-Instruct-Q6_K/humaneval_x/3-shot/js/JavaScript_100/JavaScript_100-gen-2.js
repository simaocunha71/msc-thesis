  var result = [];
  var level = n;
  while (level > 0) {
    result.unshift(level);
    level = level % 2 == 0 ? level + 1 : level - 1;
  }
  return result;
}