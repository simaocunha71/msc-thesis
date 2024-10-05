  var appleCount = parseInt(s.substring(0, s.indexOf("apples")));
  var orangeCount = parseInt(s.substring(s.indexOf("and") + 4, s.indexOf("oranges")));
  return n - appleCount - orangeCount;
}