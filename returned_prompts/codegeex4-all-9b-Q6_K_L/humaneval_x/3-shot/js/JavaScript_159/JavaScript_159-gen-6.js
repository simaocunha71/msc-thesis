  var after_meals = number + need;
  var left = remaining - need;
  if (left < 0) {
    left = 0;
  }
  return [after_meals, left];
}

console.log(eat(5, 6, 10));
console.log(eat(4, 8, 9));
console.log(eat(1, 10, 10));
console.log(eat(2, 11, 5));