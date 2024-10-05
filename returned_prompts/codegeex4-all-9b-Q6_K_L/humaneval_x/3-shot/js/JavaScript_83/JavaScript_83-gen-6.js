  var total = 9;
  var count = 0;

  for (let i = 0; i < n - 2; i++) {
    total *= 9;
  }

  if (n > 1) {
    count += total;
  }

  if (n > 2) {
    count += total;
  }

  return count;
}

console.log(startsOneEnds(3));
console.log(startsOneEnds(4));
console.log(startsOneEnds(5));

