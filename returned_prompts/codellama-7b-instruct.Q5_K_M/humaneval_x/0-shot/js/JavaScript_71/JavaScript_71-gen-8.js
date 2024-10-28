  // 1. Check if the sides make a valid triangle
  if (a + b < c || a + c < b || b + c < a) {
    return -1;
  }
  // 2. Calculate the semi-perimeter
  const s = (a + b + c) / 2;
  // 3. Calculate the area using Heron's formula
  return Math.sqrt(s * (s - a) * (s - b) * (s - c));
};
