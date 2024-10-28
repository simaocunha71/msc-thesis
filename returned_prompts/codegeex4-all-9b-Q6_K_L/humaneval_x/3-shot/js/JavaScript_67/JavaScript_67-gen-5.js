  var result = n;
  const apple = s.indexOf("apples");
  const orange = s.indexOf("oranges");
  var count = 0;
  if (apple !== -1) {
    count = Number(s.slice(apple - 1, apple));
    result -= count;
  }
  if (orange !== -1) {
    count = Number(s.slice(orange - 1, orange));
    result -= count;
  }
  return result;
}

