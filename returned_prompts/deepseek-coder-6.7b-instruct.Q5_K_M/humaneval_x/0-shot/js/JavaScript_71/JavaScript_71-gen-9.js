  if (a + b <= c || a + c <= b || b + c <= a) {
    return -1;
  }
  
  let s = (a + b + c) / 2;
  let area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
  
  return Number(area.toFixed(2));
}

console.log(triangleArea(3, 4, 5)); // 6.00
console.log(triangleArea(1, 2, 10)); // -1


