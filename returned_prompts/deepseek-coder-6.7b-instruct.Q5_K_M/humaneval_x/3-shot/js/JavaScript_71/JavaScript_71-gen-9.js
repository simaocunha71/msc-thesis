  if (a + b > c && a + c > b && b + c > a) {
    // Calculate the semi-perimeter
    var s = (a + b + c) / 2;
    // Use the semi-perimeter to calculate the area
    var area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
    return parseFloat(area.toFixed(2));
  } else {
    return -1;
  }
}



