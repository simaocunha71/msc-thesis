  if (a + b <= c || a + c <= b || b + c <= a) {
    return -1;
  }

  let semi_perimeter = (a + b + c) / 2;
  let area = Math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c));
  return Math.round(area * 100) / 100;
}



